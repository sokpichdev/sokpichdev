# InfoWeb iOS

> Sports & Lottery information platform with real-time live scores — available on the App Store

## Overview

InfoWeb is a production iOS app serving sports fans and lottery enthusiasts across multiple countries. Users can follow live match scores, browse league standings, track lottery results, generate predictions, and bookmark their favorite events — all with real-time WebSocket updates and full multi-language support.

## Features

### Sports
- Live match scores with real-time Socket.IO updates
- Leagues, teams, and standings browsers
- Fixtures and historical results
- Bookmark favorite matches for quick access

### Lottery
- Lottery games browsed by country
- Past result history and number lookups
- Random number generation
- Community player predictions

### News Feed
- Integrated news feed via a custom internal library

### Search & Discovery
- Global search across sports and lottery data
- Advanced lottery filtering by country with drag-and-drop ordering and persistent preferences

### Account & Profile
- Email and phone authentication with OTP and password options
- User profile management and password change
- Account deletion flow
- Forgot-password recovery

### App Experience
- Push notifications via Firebase Cloud Messaging
- Multi-language support with API-driven translations and in-app language switcher
- Dark mode toggle
- Offline detection with a no-connection overlay and request retry on reconnect
- Footer advertisements on the main tab bar

## Tech Stack

| Area | Technology |
|------|-----------|
| UI | SwiftUI (primary) with UIKit interop |
| Architecture | MVVM (Model / View / ViewModel) |
| Real-time | Socket.IO (live match scores) |
| Backend services | Firebase (Analytics, Cloud Messaging / FCM) |
| Networking | URLSession-based REST layer with AES encryption |
| Images | SDWebImageSwiftUI (50 MB memory + 200 MB disk cache) |
| Keyboard | IQKeyboardManager |
| Internal library | NewsFeedKit-iOS (proprietary Loma Technology package) |
| Connectivity | Custom NetworkMonitor / Reachability |
| Linting | SwiftLint |
| Dependency mgmt | Swift Package Manager |

## Architecture

The app is SwiftUI-first and follows MVVM throughout, with a central `RestAPI` singleton handling all HTTP requests and a generic `BaseModel<T>` wrapping every API response with status, message, and pagination metadata. The app launches directly into the main tab bar — no login wall — with login prompted only when a gated action is triggered:

```
lang not set → Language selection (first launch)
otherwise    → Main tab bar (Sports · Lottery · News · Favourites · Profile)
```

**Guest vs. authenticated access:**

| Area | Guest | Requires Login |
|------|-------|---------------|
| Sports — browse matches, leagues, standings | ✅ | |
| Sports — bookmark a match as favourite | | ✅ |
| Lottery — browse results by country | ✅ | |
| Lottery — apply saved filters | | ✅ |
| News Feed — read articles | ✅ | |
| News Feed — interact (comments, reactions) | | ✅ |
| Favourites tab | | ✅ |
| Profile & account settings | | ✅ |

Global singletons (`NavManager`, `NavigationState`, `UserPreference`) coordinate navigation and persistent preferences. A pending-request queue retries calls automatically when connectivity is restored.

## File Structure

```
InfoWebiOS/
├── App/               # Entry point, AppDelegate, environment setup
├── Modules/
│   ├── Main/          # Tab bar, footer ads, dark mode toggle
│   ├── Login/         # Email / phone auth, OTP, remember-me
│   ├── Register/      # New user registration
│   ├── ForgetPassword/
│   ├── Profile/       # Profile view, password change, account deletion
│   ├── SportTab/      # Matches, leagues, standings, fixtures, results
│   ├── Lottery/       # Countries, games, results, predictions
│   ├── FavouriteTab/  # Bookmarked sports & lotteries
│   ├── Search/        # Global search
│   ├── FilterLotteries/ # Country filter with drag-and-drop ordering
│   ├── Language/      # Language selection & API-driven translations
│   ├── SideMenu/
│   └── Contact/       # Support contact form
├── Common/
│   ├── APIManager/    # RestAPI, APIEndPoint, BaseModel, AES encryption
│   ├── CustomView/    # Shared UI: Toast, LoadingView, NoConnectionView,
│   │                  # MaterialTextField, RadioButton, SegmentedControl…
│   ├── Extension/     # String, Date, Int, UIFont, Color helpers
│   ├── NetworkMonitor/
│   ├── Socket/        # PusherSocketInfoWeb (Socket.IO wrapper)
│   └── Utilities/     # Singleton managers, UserPreference, NavManager
└── Resources/         # Assets, Fonts, Firebase config, bridging header
```

## Highlights

- Shipped to the App Store and used by real sports fans and lottery followers across multiple countries
- Production codebase developed and maintained by a multi-engineer team at Loma Technology Cambodia
- Real-time live match scores via Socket.IO WebSocket streaming
- Multi-environment build configs — Dev, SIT, UAT, and Production
- AES-128/256 encryption on API communication
- Pending-request retry queue that fires automatically on network recovery
- Drag-and-drop lottery filter preferences persisted across sessions
- 13 feature modules, 15+ ViewModels, 200+ Swift files

## Screenshots

<p align="center">
  <img src="assets/luckyinfo/sports.png" width="160"/>
  <img src="assets/luckyinfo/football_match_stats.png" width="160"/>
  <img src="assets/luckyinfo/news.png" width="160"/>
  <img src="assets/luckyinfo/filter.png" width="160"/>
  <img src="assets/luckyinfo/language_selection.png" width="160"/>
</p>
## Links

- [App Store](https://apps.apple.com/kh/app/luckyinfos/id6477772364)