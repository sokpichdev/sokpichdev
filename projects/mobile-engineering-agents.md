# Mobile Engineering Agents

> Turn your AI coding agent into a Senior/Staff mobile engineer — open-source, MIT licensed

## Overview

Mobile Engineering Agents is a drop-in knowledge system that gives **Claude Code, Codex, Cursor, Windsurf, Gemini CLI, and Aider** the judgment of an experienced mobile team — architecture, security, testing, and standards — so the code they generate is production-grade, not just plausible.

AI agents can write a lot of mobile code, fast. The bottleneck isn't typing — it's **engineering judgment**: picking the right architecture, getting concurrency and error handling right, securing data, and keeping the codebase maintainable as it grows. This repo encodes that judgment as machine-loadable agents, skills, workflows, checklists, templates, prompts, standards, and architecture references.

Primary focus is **iOS / Swift / SwiftUI**; secondary support for Android/Kotlin and Flutter. It's not a tutorial or handbook — it's an operational toolkit you point your AI agent at.

> **Without this toolkit:** "Build me a login screen" → a Massive View Controller with the token in `UserDefaults` and no tests.
>
> **With it:** the agent acts as a Security Expert + SwiftUI Expert — OAuth2 + PKCE, Keychain storage, MVVM, typed errors, and unit tests — then self-reviews against a checklist.

## What's Inside

| Directory | What it gives your agent | Count |
|-----------|--------------------------|-------|
| 🤖 `agents/` | Loadable expert roles (architect, security, testing…) | 14 |
| 🧠 `skills/` | Deep, single-topic know-how (auth, websockets, caching…) | 31 |
| 🔄 `workflows/` | Step-by-step procedures (build a feature, integrate an API…) | 11 |
| ✅ `checklists/` | Objective, automatable review gates | 8 |
| 📐 `standards/` | Non-negotiable rules (coding, security, testing, git) | 7 |
| 🏛️ `architecture/` | Reference designs with Mermaid diagrams | 6 |
| ✍️ `prompts/` | Copy-paste prompts for common tasks | 10 |
| 🧩 `templates/` | Scaffolding with boilerplate Swift | 8 |
| 📲 `examples/` | Reference apps (banking, chat, CoffeeCraft, ecommerce, social) | 5 |

Plus `AGENTS.md` (orchestration), `GLOSSARY.md` (shared terms), and a `README.md` index inside every directory.

## The Agent Team

Each agent is a self-contained role with purpose, responsibilities, hard rules, coding standards, a review checklist, and example tasks — organized into four tiers that hand off to each other:

| Tier | Agents |
|------|--------|
| 🧭 Strategy | System Design Expert, iOS Architect |
| 🛠️ Implementation | SwiftUI Expert, Networking Expert, WebSocket Expert, Backend Integrator |
| 🛡️ Quality & Hardening | Security Expert, Testing Expert, Performance Expert, Accessibility Expert, Refactoring Expert |
| 🚦 Gate & Delivery | Code Reviewer, Release Manager, DevOps Expert |

## How It Works

You describe a **task**; the toolkit handles the assignment. The entry file classifies your request by its *primary deliverable* (architecture, UI, data, security, a test, a release), picks the **entry agent** that owns it, and hands off down a tier chain that ends in a checklist self-review. You don't pick the agent — the request does.

| You ask for… | Entry agent | Typical chain |
|--------------|-------------|---------------|
| A login / token flow | Security Expert | Architect → Security → Networking → Testing → Reviewer |
| A new screen or UI change | SwiftUI Expert | SwiftUI → Accessibility → Testing → Reviewer |
| A new/changed API integration | Backend Integrator | Backend → Networking → Security → Testing → Reviewer |
| "It's slow / janky" | Performance Expert | Performance → specialist → Testing |

A non-trivial feature flows through multiple agents:

```mermaid
flowchart LR
    R[Feature Request] --> A[iOS Architect]
    A --> U[SwiftUI Expert]
    U --> N[Networking Expert]
    N --> S[Security Expert]
    S --> T[Testing Expert]
    T --> C[Code Reviewer]
    C --> Done([Merge-ready])
```

## Use It

```bash
# Clone it next to (or inside) your project
git clone https://github.com/sokpichdev/mobile-engineering-agents.git
```

There are two ways to drive it:

**Mode A — just describe the task** (the default, zero file paths). Editors like Cursor, Windsurf, Claude Code, and Gemini CLI auto-load the matching config file (`.cursorrules`, `.windsurfrules`, `CLAUDE.md`, `GEMINI.md`), so the defaults apply with no setup:

```text
> Build an Account Summary screen that loads /accounts and stores the auth token securely.
```

**Mode B — name a file to steer it** (optional, for precision or to override routing):

```text
> Read agents/ios_architect.md and act as that agent.
> Follow workflows/create_feature.md to build an Account Summary screen,
  then self-review against checklists/code_review.md.
```

## Design Principles

- **Clean Architecture + MVVM** and **SOLID** by default
- **Security is a requirement, not an afterthought** (OWASP MASVS)
- **Testable, modular, observable** code with explicit, typed error handling
- **Consistent standards** across sessions, tools, and contributors

## Highlights

- **Tool-agnostic** — one knowledge base works across Claude Code, Codex, Cursor, Windsurf, Gemini CLI, and Aider
- **Routing without effort** — plain-language requests are classified and routed to the right expert chain automatically
- **Self-reviewing** — every task ends against an objective checklist, so output is merge-ready, not just plausible
- **Open source & contribution-friendly** — MIT licensed, with `good first issue`s and section templates for new contributors

## Links

- [GitHub Repository](https://github.com/sokpichdev/mobile-engineering-agents)
- [Quick Start](https://github.com/sokpichdev/mobile-engineering-agents#-quick-start)
- [Contributing & Good First Issues](https://github.com/sokpichdev/mobile-engineering-agents/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- [License (MIT)](https://github.com/sokpichdev/mobile-engineering-agents/blob/main/LICENSE)
