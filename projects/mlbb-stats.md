# MLBB MetaSight

> Mobile Legends: Bang Bang companion app — hero stats, rankings, counters, and a Metal-powered splash screen

## Overview

MLBB MetaSight is a SwiftUI iOS app for browsing Mobile Legends: Bang Bang hero data — stats, rankings, lane positions, skill combos, counter matchups, and more. It features a gold-on-navy themed UI, a Metal-powered animated splash screen, offline caching, in-game user login with match history, and full localization across 16 languages served at runtime.

## Features

### Hero Data
- **Hero list** — full roster with avatar/minimap icons and infinite-scroll pagination
- **Rankings** — win, appearance, and ban rates filterable by rank tier with sorting
- **Positions** — filter by lane and class with flip-card presentation
- **Hero detail** — 7 tabs: Overview (splash art, lore, skills with video previews), Stats, Skill Combos, Trends, Counters, Relations, and Compatibility
- **Academy** — equipment, battle spells, and emblem sets
- **Search** — cross-module hero search

### User & Social
- **MLBB in-game login** — Role ID + Zone ID + verification code → JWT
- **Profile drawer** — slide-out drawer with stats, win-rate ring, and edge-swipe gesture
- **Match history** — paginated list with season filter and per-match scoreboard
- **Frequent heroes** and **friends list** with season pickers
- **Favorite heroes** stored locally
- **Privacy settings** to toggle profile visibility

### Platform
- **16-language localization** (EN, KM, ZH, ZH-TW, TH, ID, VI, MS, PT, ES, AR, TR, KO, JA, RU, DE) loaded at runtime
- **Offline cache** — file-based JSON caching with staleness indicators and network-aware refresh
- **Metal splash** — animated launch with particle spiral and ring flare, with a SwiftUI fallback for Reduce Motion / non-Metal devices

## Tech Stack

| Area | Technology |
|------|-----------|
| UI | SwiftUI |
| Architecture | MVVM (View / ViewModel / Model per module) |
| Min iOS | 16+ |
| Networking | `async/await` + `URLSession` via `NetworkService` |
| Endpoints | Typed `MLBBResource` enums conforming to `MLBBEndpoint` |
| Caching | File-based JSON via `CacheService` (per-view, per-filter) |
| Connectivity | `NWPathMonitor` via a `NetworkMonitor` singleton |
| Graphics | Metal shaders for the launch splash |
| Auth | JWT stored in `KeychainService` |
| Localization | Runtime translations via `LocalizationManager` |
| Typography | Cinzel display font (OFL) |

## Architecture

The app follows MVVM with a clear separation between networking, services, theming, reusable components, and feature modules. Data is fetched with `async/await` through a typed endpoint layer (`MLBBResource`), wrapped by `NetworkService`, and cached per-view/per-filter by `CacheService` so the app stays usable offline. A `NetworkMonitor` singleton drives network-aware refresh and staleness indicators.

Theming is centralized in a `Theme/` layer (color, font, spacing, radius tokens) and consumed by reusable themed primitives like `PanelCard`, `BannerHeader`, and `GoldDivider`.

## File Structure

```
MLBB MetaSight/
├── Constant/         # API base URL and URL builders
├── Networking/       # Typed endpoints (MLBBResource), response envelopes, pagination
├── Services/         # High-level fetch methods (APIService)
├── Utilize/          # NetworkService, CacheService, NetworkMonitor, logging
├── Launch/           # Metal splash (MTKView + Shaders/Splash.metal) + SwiftUI fallback
├── Theme/            # Color/font/spacing/radius tokens, Cinzel fonts
├── Customization/    # Reusable themed primitives + UI components (shimmer, toast, FlipView)
└── Module/
    ├── Home/         # Hero list with pagination
    ├── Ranking/      # Rankings by tier with filters
    ├── Position/     # Heroes by lane/class (flip cards)
    ├── Academy/      # Equipment, spells, emblems
    ├── Detail/       # 7-tab hero detail
    ├── Search/       # Cross-module hero search
    └── User/         # Auth, profile, match history, friends (Model/View/ViewModel)
```

## Highlights

- **Metal-rendered splash** with particle spiral and ring flare — GPU graphics beyond standard SwiftUI animation, with an accessibility-aware fallback
- **Offline-first caching** keeps the app usable without a connection and surfaces data staleness
- **16-language runtime localization** loaded remotely, with a centralized key registry
- **Full MLBB account integration** — in-game verification login, match history, and friends
- Clean, token-driven theming system reused across every feature module

## Screenshots

<p align="center">
  <img src="assets/mlbb-stats/screenshot-1.png" width="240"/>
  <img src="assets/mlbb-stats/screenshot-2.png" width="240"/>
  <img src="assets/mlbb-stats/screenshot-3.png" width="240"/>
</p>

> _Add screenshots to `projects/assets/mlbb-stats/` and update the filenames above. The Metal splash and 7-tab hero detail make strong shots._

## Credits

Hero data provided by the open-source [ridwaanhall/api-mobilelegends](https://github.com/ridwaanhall/api-mobilelegends). MLBB game assets are property of Moonton.

## Links

- [GitHub](https://github.com/cobra-PICH/mlbb-stats)
