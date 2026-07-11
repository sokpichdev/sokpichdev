<h1 align="center">MLBB MetaSight</h1>

<p align="center">
  <strong>Mobile Legends: Bang Bang companion app — hero stats, rankings, counters, and a Metal-powered splash screen</strong><br/>
  <sub>Gold-on-navy themed UI, offline caching, in-game account login, and full localization across 16 languages served at runtime.</sub>
</p>

<p align="center">
  <img alt="Platform" src="https://img.shields.io/badge/platform-iOS%2017%2B-blue"/>
  <img alt="Language" src="https://img.shields.io/badge/Swift-5.9-orange"/>
  <img alt="UI" src="https://img.shields.io/badge/UI-SwiftUI-green"/>
  <img alt="Status" src="https://img.shields.io/badge/status-in%20development-yellow"/>
  <img alt="" src="https://komarev.com/ghpvc/?username=sokpichdev&color=blueviolet"/>
</p>

---

## Table of Contents

- [Screenshots](#screenshots)
- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
- [Testing](#testing)
- [CI/CD](#cicd)
- [Privacy & Permissions](#privacy--permissions)
- [Accessibility](#accessibility)
- [Localization](#localization)
- [Project Status](#project-status)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Credits](#credits)
- [Author](#author)

---

## Screenshots

**Launch & Auth**

| Splash Screen | Login |
|---|---|
| <img src="assets/mlbb-stats/splash_screen.png" width="160"/> | <img src="assets/mlbb-stats/login_screen.png" width="160"/> |
| Metal-rendered particle spiral and ring flare launch animation | MLBB in-game login via Game ID, Server ID, and verification code |

**Heroes**

| Hero List | Heroes Flow | Hero Rankings |
|---|---|---|
| <img src="assets/mlbb-stats/heroes_list.png" width="160"/> | <img src="assets/mlbb-stats/heroes_flow.png" width="160"/> | <img src="assets/mlbb-stats/hero_rankings.png" width="160"/> |
| Full hero roster with avatar icons and infinite-scroll pagination | Navigation flow between hero list and detail views | Win rates, pick rates, and ban rates filterable by rank tier |

| Hero Positions | Hero Search | Hero Favorite |
|---|---|---|
| <img src="assets/mlbb-stats/hero_positions.png" width="160"/> | <img src="assets/mlbb-stats/hero_search.png" width="160"/> | <img src="assets/mlbb-stats/hero_favorite.png" width="160"/> |
| Heroes filtered by lane and role with flip-card presentation | Cross-module hero search | Locally stored favorite heroes |

**Academy**

| Ranks | Recommended | Battle Spells |
|---|---|---|
| <img src="assets/mlbb-stats/academy_ranks.png" width="160"/> | <img src="assets/mlbb-stats/academy_recommended.png" width="160"/> | <img src="assets/mlbb-stats/academy_spells.png" width="160"/> |
| Rank-tier breakdown and progression guidance | Recommended equipment builds | Battle spell reference |

| Emblems |
|---|
| <img src="assets/mlbb-stats/academy_emblems.png" width="160"/> |
| Emblem set reference |

**User Profile**

| Side Menu (Guest) | Side Menu (User) | User Stats |
|---|---|---|
| <img src="assets/mlbb-stats/side_menu_guest.png" width="160"/> | <img src="assets/mlbb-stats/side_menu_user.png" width="160"/> | <img src="assets/mlbb-stats/user_stats.png" width="160"/> |
| Slide-out drawer before login | Slide-out drawer with stats and win-rate ring after login | Win-rate ring and season-filtered account stats |

| Frequent Heroes | Friends | Match History |
|---|---|---|
| <img src="assets/mlbb-stats/frequent_heroes.png" width="160"/> | <img src="assets/mlbb-stats/friends.png" width="160"/> | <img src="assets/mlbb-stats/matches_history.png" width="160"/> |
| Most-played heroes with season picker | Friends list with season picker | Paginated match history with per-match scoreboard |

| Match History Filter |
|---|
| <img src="assets/mlbb-stats/matches_history_filter.png" width="160"/> |
| Season filter for match history |

**Hero Detail**

| Overview | Stats | Counters |
|---|---|---|
| <img src="assets/mlbb-stats/hero_detail_overview.gif" width="160"/> | <img src="assets/mlbb-stats/hero_detail_stats.gif" width="160"/> | <img src="assets/mlbb-stats/hero_detail_counters.gif" width="160"/> |
| Splash art, lore, and skills with video previews | Hero stat breakdown | Counter matchups |

| Skill Combos | Compatibility | Relations |
|---|---|---|
| <img src="assets/mlbb-stats/hero_detail_skills_combo.gif" width="160"/> | <img src="assets/mlbb-stats/hero_detail_compatibility.png" width="160"/> | <img src="assets/mlbb-stats/hero_detail_relations.png" width="160"/> |
| Recommended skill combo sequences | Compatibility with other heroes | Synergy and relation mapping |

**Settings & Filters**

| Settings | Content Language | Filter Sheet |
|---|---|---|
| <img src="assets/mlbb-stats/settings.png" width="160"/> | <img src="assets/mlbb-stats/content_language.png" width="160"/> | <img src="assets/mlbb-stats/fliter_sheet.png" width="160"/> |
| App settings and privacy toggles | Runtime language selection across 16 supported languages | Shared filter sheet used across ranking and position views |

---

## Features

### Hero Data
- **Hero list** — full roster with avatar/minimap icons and infinite-scroll pagination
- **Rankings** — win rates, pick rates, and ban rates filterable by rank tier with sorting
- **Positions** — filter by lane and role with flip-card presentation
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

---

## Demo

<!-- No standalone demo GIF file exists yet — the animated Hero Detail tabs (Overview, Stats, Counters, Skill Combos) above are already captured as GIFs in Screenshots. -->

The Metal-rendered splash screen (particle spiral + ring flare) and the Hero Detail tabs are the two most visually distinctive flows — see the GIFs under [Screenshots → Hero Detail](#screenshots).

---

## Tech Stack

| Layer | Choice |
|---|---|
| **Language** | Swift 5.9 |
| **UI** | SwiftUI |
| **Architecture** | MVVM (`Module/` — View / ViewModel / Model per feature) |
| **Concurrency** | Swift Concurrency (`async`/`await`) |
| **Networking** | `URLSession` via `NetworkService`, typed `MLBBResource`/`MLBBEndpoint` |
| **Realtime** | Firestore (remote config for the Top Up promo only) |
| **Persistence** | File-based JSON cache (`CacheService`), Keychain (`KeychainService`) |
| **Backend / BaaS** | Custom API (`mlbb.rone.dev`) + Firebase (Analytics, Firestore for Top Up config) |
| **Dependencies** | Swift Package Manager |
| **Analytics** | Firebase Analytics (Measurement Protocol, optional) |
| **Graphics** | Metal shaders for the launch splash |
| **Auth** | JWT via `KeychainService`; MLBB in-game verification flow |
| **Typography** | Cinzel display font (OFL licensed) |
| **Min iOS** | 17+ |

---

## Architecture

MVVM per feature module, with a shared services layer (networking, caching, auth) that every module's ViewModel depends on. The `TopUp` module is the one exception — it talks to Firestore directly for its remote promo config rather than going through the API service layer.

```mermaid
graph TD
    Views["Module Views (Home / Ranking / Detail / User / TopUp / ...)"] --> ViewModels["ViewModels"]
    ViewModels --> APIService["APIService"]
    APIService --> NetworkService["NetworkService (URLSession)"]
    APIService --> CacheService["CacheService (File-based JSON)"]
    ViewModels --> KeychainService["KeychainService (JWT/Auth)"]
    NetworkService --> API["mlbb.rone.dev"]
    ViewModels --> Firestore["Firestore (Top Up promo config)"]
```

**Key decisions**
- Each feature module under `Module/` owns its own View / ViewModel / Model — no shared cross-feature state beyond the services layer.
- All async work goes through Swift Concurrency (`async`/`await`); no Combine.
- The `TopUp` module bypasses `APIService`/`NetworkService` and reads its config straight from Firestore, since the promo is unrelated to hero data and needs to be toggled without an App Store release.

---

## Folder Structure

```
MLBB MetaSight/
├── Constant/
│   └── APIConstants.swift          # Base URL and URL builders
├── Networking/
│   ├── APIResource.swift           # Typed endpoint definitions (MLBBResource)
│   ├── APIResponse.swift           # Response envelope types
│   └── PageQuery.swift             # Pagination query builder
├── Services/
│   └── APIService.swift            # High-level fetch methods
├── Utilize/
│   ├── NetworkService.swift        # URLSession wrapper
│   ├── CacheService.swift          # File-based JSON cache
│   ├── NetworkMonitor.swift        # NWPathMonitor connectivity
│   ├── DebugURLProtocol.swift      # Request logging (debug builds)
│   └── LogWriter.swift
├── Launch/
│   ├── LaunchScreen.storyboard     # Static themed launch screen
│   ├── SplashGate.swift            # Gate between splash and app
│   ├── SwiftUISplashView.swift     # Fallback splash (radial glow + fade)
│   ├── MetalSplashView.swift       # MTKView-backed animated splash
│   ├── SplashRenderer.swift        # Metal renderer (particles + ring flare)
│   └── Shaders/Splash.metal        # Metal shader
├── Theme/
│   ├── MLBBColor.swift             # Color tokens (gold, navy, panel)
│   ├── MLBBFont.swift              # Typography (Cinzel + system)
│   ├── MLBBSpacing.swift           # Spacing scale
│   ├── MLBBRadius.swift            # Corner radius tokens
│   ├── ThemeAppearance.swift       # UIKit appearance configuration
│   └── Fonts/                      # Cinzel-Regular.ttf, Cinzel-Bold.ttf
├── Customization/
│   ├── Theme/                      # Reusable themed primitives
│   │   ├── PanelCard.swift         # Gradient panel with gold hairline
│   │   ├── BannerHeader.swift      # Cinzel uppercase section header
│   │   ├── GoldDivider.swift       # 1pt gradient divider
│   │   ├── ThemedButtonStyle.swift # Primary/secondary button styles
│   │   └── RankTier.swift          # Tier-to-color mapping
│   ├── API_UI_Components/          # Shimmer, toast, staleness indicator
│   ├── FlipView.swift
│   ├── FlowLayout.swift
│   ├── HTMLWebView.swift
│   └── ...
└── Module/
    ├── Home/                       # Hero list with pagination
    ├── Ranking/                    # Rankings by tier with filters
    ├── Position/                   # Heroes by lane/class (flip cards)
    ├── Academy/                    # Equipment, spells, emblems
    ├── Detail/                     # 7-tab hero detail
    │   └── View/Tabs/             # Overview, Stats, SkillCombos, Trends,
    │                               # Counters, Relations, Compatibility
    ├── Search/                     # Cross-module hero search
    ├── Favorites/                  # Locally stored favorite heroes
    ├── TopUp/                      # Diamond top-up affiliate promotion
    └── User/                       # Auth, profile, match history, friends
        ├── Model/                  # DTOs: auth, info, stats, matches, friends
        ├── View/                   # LoginView, ProfileView, MatchHistoryView,
        │                           # FrequentHeroesView, FriendsView, PrivacySettingsView
        └── ViewModel/               # AuthViewModel, ProfileViewModel, UserSettingsViewModel
```

> **Note:** the repo root also contains a legacy `MLBB Hero Insight.xcodeproj`. It is a stale artifact from before the project was renamed and is not the active project — always open `MLBB MetaSight.xcodeproj`.

---

## Getting Started

### Requirements
- macOS with Xcode 15+
- Target: iOS 17+
- No API key required for hero/academy/user data

### Clone
```bash
git clone https://github.com/sokpichdev/mlbb-stats.git
cd mlbb-stats
```

### Configuration

Hero, academy, and user data need no configuration — they're fetched from the public API at `https://mlbb.rone.dev`.

The **Top Up** feature reads its promo config from Firestore and reports to Firebase Analytics, which need real Firebase credentials:
```bash
cp Secrets.xcconfig.example Secrets.xcconfig
```

| Key | Purpose | Required |
|---|---|---|
| `FIREBASE_APP_ID` | Firebase app identifier (Top Up / Analytics) | ⚪ only for Top Up |
| `FIREBASE_API_SECRET` | Measurement Protocol API secret (Top Up / Analytics) | ⚪ only for Top Up |

### Install dependencies / Run
Open `MLBB MetaSight.xcodeproj` in Xcode 15+ (Swift Package Manager dependencies resolve automatically), select a simulator or device running iOS 17+, and run.

> Ignore `MLBB Hero Insight.xcodeproj` at the repo root — it's a legacy project file left over from before the app was renamed.

---

## Testing

```bash
xcodebuild test -scheme "MLBB MetaSight" -destination 'platform=iOS Simulator,name=iPhone 15'
```

- **Unit tests** (`MLBB MetaSightTests/`): `APIResource`, `APIResponse`, `AppLanguage`, `AuthViewModel`, `CacheService`, `DrawerSnapDecision`, `HeroModel`, `HomeViewModel`, `KeychainService`, `LocalizationManager`, `NetworkService`, `PageQuery`, `SearchViewModel`, `TopUpConfig`, `TopUpService`, `TopUpViewModel`
- **UI tests** (`MLBB MetaSightUITests/`): Home, Search, and general app flows
- **Coverage target:** none set yet — TODO
- **Test doubles:** ad hoc per test; no shared mocking framework in place — TODO

---

## CI/CD

No CI/CD is configured yet — there's no `.github/workflows/` and no `fastlane/` setup. Tests currently run locally via Xcode/`xcodebuild` only. — **TODO**

---

## Privacy & Permissions

- No OS-level permissions (camera, location, notifications, etc.) are currently requested by the app.
- **Data collected:** none beyond optional Firebase Analytics events for the Top Up promotion (Measurement Protocol). No PII is sold or shared.
- **Third parties:** Firebase (Analytics, Firestore — Top Up feature only), the public hero/user API at `mlbb.rone.dev`.
- **Full policy:** no standalone privacy policy document exists yet — **TODO**

---

## Accessibility

Accessibility has not been formally audited yet — VoiceOver labeling, Dynamic Type scaling, contrast ratios, and Reduce Motion support beyond the splash-screen fallback are best-effort, not verified. — **TODO**

---

## Localization

Supported languages: English, Chinese (Simplified & Traditional), Thai, Indonesian, Vietnamese, Malay, Portuguese, Spanish, Arabic, Turkish, Korean, Japanese, Russian, German, Khmer (16 total).

Strings are served at runtime from GitHub Pages and loaded by `LocalizationManager`, resolved via the `LocalizeKey` registry and `L10n` (see [Folder Structure](#folder-structure)).

---

## Project Status

🚧 In active development — hero browsing, rankings, positions, detail tabs, academy, search, favorites, diamond top-up promotion, and full user auth/profile/match-history flows are implemented; ongoing polish and API coverage.

---

## Roadmap

- [ ] Item builds and full equipment simulation
- [ ] Widget / Live Activity support
- [ ] watchOS companion

---

## Contributing

No `CONTRIBUTING.md` exists yet — **TODO**. In the meantime:
1. Fork and create a feature branch (`git checkout -b feat/thing`)
2. Commit using [Conventional Commits](https://www.conventionalcommits.org/)
3. Open a PR against `main`

---

## Security

No standalone `SECURITY.md` exists yet — **TODO**. Current security documentation lives in the repo at [`SECURITY_REVIEW.md`](https://github.com/sokpichdev/mlbb-stats/blob/main/SECURITY_REVIEW.md) and [`SECURITY_REMEDIATION_PLAN.md`](https://github.com/sokpichdev/mlbb-stats/blob/main/SECURITY_REMEDIATION_PLAN.md).

---

## License

This project is for personal / educational use. MLBB game assets (hero names, images, skills) are property of Moonton. No standalone `LICENSE` file exists yet.

---

## Acknowledgments

- **Cinzel** display font — [SIL Open Font License](https://openfontlicense.org/)

---

## Credits

Hero data provided by the open-source [ridwaanhall/api-mobilelegends](https://github.com/ridwaanhall/api-mobilelegends). MLBB game assets are property of Moonton.

---

## Author

**Sok Pich** — [@sokpichdev](https://github.com/sokpichdev)
