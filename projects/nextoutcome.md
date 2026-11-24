<p align="center">
  <img src="assets/nextoutcome/app_icon.png" alt="NextOutcome app icon" width="120"/>
</p>

<h1 align="center">NextOutcome</h1>

<p align="center">
  <strong>Polymarket, built native for iOS — live prediction markets, real-time order books, and purpose-built hubs for Sports, Crypto, Esports, Politics and the World Cup</strong><br/>
  <sub>Solo project, designed and built end to end. Read-only today; on-chain trading is next.</sub>
</p>

<p align="center">
  <img alt="Platform" src="https://img.shields.io/badge/platform-iOS%2018%2B-blue"/>
  <img alt="Swift" src="https://img.shields.io/badge/Swift-5.9-orange"/>
  <img alt="UI" src="https://img.shields.io/badge/UI-SwiftUI-green"/>
  <img alt="Architecture" src="https://img.shields.io/badge/Clean%20Architecture-MVVM-green"/>
  <img alt="Tests" src="https://img.shields.io/badge/tests-800%2B%20passing-brightgreen"/>
  <a href="https://testflight.apple.com/join/cPNP7B6D"><img alt="TestFlight" src="https://img.shields.io/badge/TestFlight-join%20the%20beta-0D96F6?logo=apple&logoColor=white"/></a>
  <img alt="" src="https://komarev.com/ghpvc/?username=sokpichdev&color=blueviolet"/>
</p>

<p align="center">
  <b>Try it on your iPhone →</b> <a href="https://testflight.apple.com/join/cPNP7B6D">testflight.apple.com/join/cPNP7B6D</a>
</p>

---

## Table of Contents

- [Why NextOutcome](#why-nextoutcome)
- [Screenshots](#screenshots)
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Engineering Highlights](#engineering-highlights)
- [Privacy & Permissions](#privacy--permissions)
- [Project Status](#project-status)
- [Author](#author)

---

## Why NextOutcome

[Polymarket](https://polymarket.com) lives in a browser. NextOutcome brings its markets, order books and live sports data to a proper native iOS app: smooth feeds, real-time WebSocket order books, live charts, and category hubs that each get a layout suited to that category instead of one generic list. No wallet is needed to explore. Browsing, order books, live stats and portfolio tracking are all watch-only today.

---

## Screenshots

**Home & Feeds**

| Home — "All" | Home — Politics | Search | Breaking — 24h movers |
|---|---|---|---|
| <img src="assets/nextoutcome/home_trending.png" width="160"/> | <img src="assets/nextoutcome/home_politics.png" width="160"/> | <img src="assets/nextoutcome/search.png" width="160"/> | <img src="assets/nextoutcome/breaking_movers.png" width="160"/> |

**Market Detail & Trading**

| Multi-outcome market | Live order book | Binary market — chart & book | Trade sheet | Discussion |
|---|---|---|---|---|
| <img src="assets/nextoutcome/market_detail.png" width="160"/> | <img src="assets/nextoutcome/orderbook_live.png" width="160"/> | <img src="assets/nextoutcome/worldcup_franch_winner.png" width="160"/> | <img src="assets/nextoutcome/trade_confirm_alert.png" width="160"/> | <img src="assets/nextoutcome/discuss_sheet.png" width="160"/> |

**Sports**

| Live feed | Futures | Live now | MLB league | Wimbledon |
|---|---|---|---|---|
| <img src="assets/nextoutcome/home_sports_live.png" width="160"/> | <img src="assets/nextoutcome/home_sports_futures.png" width="160"/> | <img src="assets/nextoutcome/sports_hub_catalogue.png" width="160"/> | <img src="assets/nextoutcome/home_sports_mlb.png" width="160"/> | <img src="assets/nextoutcome/home_sports_wimbledon.png" width="160"/> |

**World Cup**

| Games | Bracket | Props | SceneKit globe | Winner odds |
|---|---|---|---|---|
| <img src="assets/nextoutcome/home_worldcup_game.png" width="160"/> | <img src="assets/nextoutcome/home_worldcup_bracket.png" width="160"/> | <img src="assets/nextoutcome/home_worldcup_props.png" width="160"/> | <img src="assets/nextoutcome/home_worldcup_map.png" width="160"/> | <img src="assets/nextoutcome/home_trending_worldcup_winners.png" width="160"/> |

**Crypto, Esports & Politics**

| Crypto hub | Crypto live window | Live book & trades | Esports hub | Esports match |
|---|---|---|---|---|
| <img src="assets/nextoutcome/crypto_hub.png" width="160"/> | <img src="assets/nextoutcome/crypto_live.png" width="160"/> | <img src="assets/nextoutcome/crypto_live_sections.png" width="160"/> | <img src="assets/nextoutcome/esports_hub.png" width="160"/> | <img src="assets/nextoutcome/esports_match_detail.png" width="160"/> |

| Politics hub — Midterms map | Senate & House seats |
|---|---|
| <img src="assets/nextoutcome/politics_hub.png" width="160"/> | <img src="assets/nextoutcome/politics_midterm_election.png" width="160"/> |

---

## Demo

| Home feed | Sports hub | Esports hub | Crypto hub |
|---|---|---|---|
| <img src="assets/nextoutcome/home_all_listing.gif" width="160"/> | <img src="assets/nextoutcome/sports_hub.gif" width="160"/> | <img src="assets/nextoutcome/esports_hub.gif" width="160"/> | <img src="assets/nextoutcome/crypto_hub.gif" width="160"/> |

| Crypto — Price | Crypto — Chance | Crypto — Candles | Politics — Midterms |
|---|---|---|---|
| <img src="assets/nextoutcome/crypto_price.gif" width="160"/> | <img src="assets/nextoutcome/crypto_chance.gif" width="160"/> | <img src="assets/nextoutcome/crypto_candles.gif" width="160"/> | <img src="assets/nextoutcome/politics_midterm_election.gif" width="160"/> |

| World Cup hub | World Cup — 3D globe |
|---|---|
| <img src="assets/nextoutcome/home_world_cup.gif" width="160"/> | <img src="assets/nextoutcome/home_worldcup_map.gif" width="160"/> |

---

## Features

### Shell & Navigation
- Three primary tabs (Home, Breaking, Portfolio), Search as a standalone `Tab(role: .search)`, and a slide-in drawer. Each tab owns its own `NavigationStack`
- Markets feed with a server-driven category rail, sort/status filters and infinite scroll
- Debounced full-text search
- App-wide light/dark theme toggle, persisted locally and independent of the system setting
- Shaped shimmer skeletons for every loading state, and numbers that roll digit by digit when they change

### Market Detail & Order Book
- Multi-series price chart with selectable timeframes, a "% chance" header, grouped market sections (moneyline / spreads / totals) and a sticky header
- Yes/No trade bar pinned to the bottom of the screen
- **Live order book** streamed over WebSocket with transparent reconnect/back-off, spread and cumulative depth bars
- Comments, top holders and recent activity in a swipe-to-dismiss Discuss sheet

### Category Hubs
- **Sports** — a server-driven sport → league catalogue (not hardcoded), a Live feed paged and sectioned by date (*Live now / Starting soon / Today / Tomorrow*), live clocks and scores, standings, team profiles, and eight odds formats (cents, American, decimal, fractional, and more)
- **World Cup** — games schedule, props, a bracket carousel, and a rotating, draggable **SceneKit globe** of nation odds
- **Crypto** — Up/Down, Above/Below, Price Range and Hit Price markets. Up/Down opens a **live window screen**: a countdown synced to the server clock, price-to-beat delta, Price/Chance/Candles charts with pinch-to-zoom, order-book depth and a recent-trades ticker. When one window closes, the screen moves to the next window without leaving the page
- **Esports** — live matches with Twitch/YouTube stream embeds behind a live-status probe, a trade ticker, a leaderboard, and scores pushed over the sports WebSocket
- **Politics (2026 Midterms)** — countdown hero, Senate/House control cards with seat pictograms, and a **US state map** coloured by race lean, drawn from parsed SVG paths with no map SDK
- **Breaking** — the biggest 24h movers, each with its own detail chart

### Live Data & Portfolio
- Live sports stats: score hero, minute timeline, stats, pitch, lineups and commentary
- **Watch-only portfolio**: track any wallet's positions, activity and the trader leaderboard. No keys, no custody

### Trading (simulated)
- Custom number pad with tactile 3D keys, a live "to win" payout, a success animation and a receipt summary. Simulated: nothing is sent or stored
- **Geoblock gate**: checks Polymarket's public geoblock status and won't open the trade sheet in blocked regions (with separate wording for close-only regions)

---

## Tech Stack

| Layer | Choice |
|---|---|
| **Language** | Swift 5.9 |
| **UI** | SwiftUI, Swift Charts, SceneKit (3D globe) |
| **Concurrency** | Swift Concurrency — `async/await`, actors, `AsyncStream` / `AsyncThrowingStream` |
| **State** | Observation (`@Observable`), MVVM view models |
| **Networking** | `URLSession` for REST **and** WebSockets (order book + sports feeds) |
| **Persistence** | Keychain (session token), `UserDefaults` (watched wallet, theme) |
| **Modularization** | Swift Package Manager — one umbrella package, 18 library modules |
| **Logging** | `os.Logger`, signposts for render-path profiling |
| **Lint** | SwiftLint, pinned in CI |
| **Backend** | Polymarket public APIs — **Gamma**, **Data**, **CLOB**, plus the sports/market WebSocket channels |
| **Dependencies** | Zero third-party packages |
| **Min target** | iOS 18+ (iPhone & iPad) |

---

## Architecture

**Clean Architecture (Domain / Data / Presentation) + MVVM.** Each feature is a vertical slice with its own `*Domain`, `*Data` and `*Presentation` modules, and the app target is a thin composition root.

```mermaid
graph TD
    UI["Presentation<br/>(SwiftUI Views / @Observable ViewModels)"] --> Domain["Domain<br/>(Use Cases / Entities / Repository protocols)"]
    Domain --> Data["Data<br/>(DTOs, mappers, repository implementations)"]
    Data --> Remote["Remote<br/>(Gamma / Data / CLOB REST + WebSocket)"]
    Data --> Local["Local<br/>(in-memory caches, Keychain, UserDefaults)"]
```

**Key decisions**
- Presentation depends only on Domain use-case protocols and never imports a feature's Data layer. A single composition root wires the concrete repositories and hands ready-made view models to the UI.
- Features never import each other; shared primitives (loading state, pagination) live in one small shared module.
- Wallet **signing** is deliberately kept out of the app until a vetted secp256k1 / EIP-712 implementation passes security review.
- View bodies are split so `@Observable` tracking stays narrow. On the crypto live screen, for example, the once-a-second countdown tick doesn't re-render the candle chart.

---

## Engineering Highlights

- **Real-time order books that survive bad networks.** The WebSocket client reconnects with back-off without the UI noticing, and a pure reducer applies snapshots and deltas, so the depth ladder is unit-tested without a socket.
- **Tolerant decoding for a messy API.** Polymarket's wire formats are inconsistent (stringified JSON arrays, mixed number/string fields, abandoned events). Dedicated decoders and filters absorb this in the Data layer, so Domain only ever sees clean entities.
- **Server-driven taxonomy.** The Sports catalogue and category rail are built from Gamma tags at runtime, so new leagues and categories appear without an app release.
- **No map SDK for maps.** The US Midterms map is drawn from parsed SVG path geometry, and the World Cup globe is a SceneKit scene with real continent outlines.
- **Measured performance work.** Signpost instrumentation and a written profiling protocol guided targeted fixes, such as cutting CPU on the crypto live screen by narrowing observation scope.
- **Tested and gated in CI.** 800+ hermetic unit tests (no simulator, no network) across every Domain, Data and Presentation layer, plus an XCUITest suite for core flows. Every PR runs the tests, SwiftLint and an app build.

---

## Privacy & Permissions

- **No permissions requested:** no camera, location or notifications.
- **No analytics or crash reporting:** zero third-party dependencies, only `os.Logger`.
- **Data entered:** an optional wallet address to watch, stored locally and sent only to Polymarket's public Data API. There is no first-party backend.

---

## Project Status

🚀 **In public beta on TestFlight.** Browsing, live order books, all five category hubs, live sports and World Cup, Breaking movers, the watch-only portfolio and theming all ship. Trading is simulated, pending a vetted on-device signer and backend proxy. The geoblock gate in front of it is real and enforced.

**Next up:** real on-chain trading (EIP-712 signer + proxy), wallet connect, push notifications for price moves and resolutions, and an App Store release.

---

## Author

**Sok Pich** — [@sokpichdev](https://github.com/sokpichdev) · [sokpich.dev](https://www.sokpich.dev/)
<sub>Solo project: product, design and iOS engineering.</sub>
