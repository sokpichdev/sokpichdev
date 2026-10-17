#!/usr/bin/env python3
# Render a tokyo-night contribution graph SVG for the profile README.
# Usage:
#   GITHUB_TOKEN=... ./contribution_graph.py                 # writes assets/contribution-graph.svg
#   GITHUB_TOKEN=... ./contribution_graph.py -u user -d 31 -o out.svg

import argparse
import json
import os
import sys
import urllib.request
from datetime import date, timedelta

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""

# Matches the tokyonight theme used by the stats and streak cards.
BG = "#1a1b27"
GRID = "#2a2e45"
TITLE = "#70a5fd"
TEXT = "#a9b1d6"
MUTED = "#565f89"
LINE = "#58a6ff"
ACCENT = "#bf91f3"

WIDTH, HEIGHT = 1000, 340
PAD_L, PAD_R, PAD_T, PAD_B = 56, 32, 92, 48


def fetch_days(login, days, token):
    end = date.today()
    start = end - timedelta(days=days - 1)
    body = json.dumps({
        "query": QUERY,
        "variables": {
            "login": login,
            "from": f"{start}T00:00:00Z",
            "to": f"{end}T23:59:59Z",
        },
    }).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        payload = json.load(resp)
    if "errors" in payload:
        sys.exit(f"GitHub API error: {payload['errors']}")
    weeks = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    counts = {d["date"]: d["contributionCount"] for w in weeks for d in w["contributionDays"]}
    return [(start + timedelta(days=i), counts.get(str(start + timedelta(days=i)), 0)) for i in range(days)]


def smooth_path(points):
    # Catmull-Rom spline converted to cubic beziers.
    d = f"M{points[0][0]:.1f},{points[0][1]:.1f}"
    for i in range(len(points) - 1):
        p0 = points[i - 1] if i > 0 else points[i]
        p1, p2 = points[i], points[i + 1]
        p3 = points[i + 2] if i + 2 < len(points) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d


def nice_max(value):
    # Round up so the four grid intervals land on whole numbers.
    for step in (1, 2, 5, 10, 15, 20, 25, 50, 100, 250, 500):
        if value <= step * 4:
            return step * 4
    return -(-value // 4) * 4


def render(login, data):
    counts = [c for _, c in data]
    total, best = sum(counts), max(counts)
    active = sum(1 for c in counts if c)
    streak = 0
    for c in reversed(counts):
        if not c:
            break
        streak += 1

    top = nice_max(best)
    plot_w = WIDTH - PAD_L - PAD_R
    plot_h = HEIGHT - PAD_T - PAD_B
    base_y = PAD_T + plot_h
    step_x = plot_w / (len(data) - 1)
    points = [(PAD_L + i * step_x, base_y - c / top * plot_h) for i, c in enumerate(counts)]
    line = smooth_path(points)
    area = f"{line} L{points[-1][0]:.1f},{base_y} L{points[0][0]:.1f},{base_y} Z"

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" '
        f'font-family="\'Segoe UI\', Ubuntu, sans-serif" role="img" aria-label="{login} contribution graph">',
        "<style>",
        f".line{{stroke-dasharray:4000;stroke-dashoffset:4000;animation:draw 2s ease-out forwards}}",
        f".fade{{opacity:0;animation:fade .8s ease-out 1.2s forwards}}",
        "@keyframes draw{to{stroke-dashoffset:0}}",
        "@keyframes fade{to{opacity:1}}",
        "</style>",
        "<defs>",
        '<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">',
        f'<stop offset="0%" stop-color="{LINE}" stop-opacity=".35"/>',
        f'<stop offset="100%" stop-color="{LINE}" stop-opacity="0"/>',
        "</linearGradient>",
        '<linearGradient id="stroke" x1="0" y1="0" x2="1" y2="0">',
        f'<stop offset="0%" stop-color="{LINE}"/>',
        f'<stop offset="100%" stop-color="{ACCENT}"/>',
        "</linearGradient>",
        "</defs>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" rx="6" fill="{BG}"/>',
        f'<text x="{PAD_L}" y="40" fill="{TITLE}" font-size="20" font-weight="600">{login}\'s Contribution Graph</text>',
        f'<text x="{PAD_L}" y="64" fill="{MUTED}" font-size="13">Last {len(data)} days · '
        f'{data[0][0]:%b %d} – {data[-1][0]:%b %d, %Y}</text>',
    ]

    stats = [("Total", total), ("Active days", active), ("Best day", best), ("Streak", streak)]
    x = WIDTH - PAD_R
    for label, value in reversed(stats):
        out.append(f'<text x="{x}" y="40" text-anchor="end" fill="{TEXT}" font-size="18" font-weight="600">{value}</text>')
        out.append(f'<text x="{x}" y="62" text-anchor="end" fill="{MUTED}" font-size="12">{label}</text>')
        x -= 110

    for i in range(5):
        value = top * i / 4
        y = base_y - plot_h * i / 4
        label = f"{value:g}"
        out.append(f'<line x1="{PAD_L}" y1="{y:.1f}" x2="{WIDTH - PAD_R}" y2="{y:.1f}" stroke="{GRID}" stroke-dasharray="{"0" if i == 0 else "3 4"}"/>')
        out.append(f'<text x="{PAD_L - 12}" y="{y + 4:.1f}" text-anchor="end" fill="{MUTED}" font-size="11">{label}</text>')

    for i, (day, _) in enumerate(data):
        if i % 3 == 0 or i == len(data) - 1:
            out.append(f'<text x="{points[i][0]:.1f}" y="{base_y + 22}" text-anchor="middle" fill="{MUTED}" font-size="11">{day.day}</text>')

    out.append(f'<path class="fade" d="{area}" fill="url(#area)"/>')
    out.append(f'<path class="line" d="{line}" fill="none" stroke="url(#stroke)" stroke-width="2.5" stroke-linecap="round"/>')
    out.append('<g class="fade">')
    for (px, py), (day, c) in zip(points, data):
        r = 4 if c == best and c else 2.5
        out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" fill="{BG}" stroke="{LINE}" stroke-width="2"><title>{day:%b %d}: {c}</title></circle>')
    out.append("</g>")
    out.append("</svg>")
    return "\n".join(out) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", default="sokpichdev")
    parser.add_argument("-d", "--days", type=int, default=31)
    parser.add_argument("-o", "--output", default="assets/contribution-graph.svg")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("Set GITHUB_TOKEN")

    svg = render(args.user, fetch_days(args.user, args.days, token))
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        f.write(svg)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
