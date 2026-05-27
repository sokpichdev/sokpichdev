# CoffeeCraft

> Production-grade coffee shop app with dual roles, real-time order pipeline, and atomic wallet transactions

## Overview

CoffeeCraft is a full-featured coffee shop iOS app built to simulate a real-world ordering system. It supports two distinct user roles — Customer and Manager — with real-time order tracking, an in-app wallet, loyalty cards, a verified reviews system, and a live admin dashboard.

## Features

### Authentication
- Email/password sign-up and sign-in via Firebase Auth
- Role selection at registration (Customer or Manager)
- Session restore on launch

### Menu & Ordering
- Product catalog grouped by category with search and chip filtering
- Dynamic drink customization (size, extras) — pricing deltas computed per option
- Cart backed by Firestore — persists across app restarts
- Store locator with MapKit showing branch pins, hours, amenities, and directions

### Wallet
- In-app wallet with balance display and scrollable transaction history
- Three-step top-up flow: Amount → Bank → Checkout
- All mutations (top-up, payment, refund) run as atomic Firestore transactions, keeping balance and ledger in sync

### Orders
- Real-time order status updates via Firestore snapshot listeners
- Cursor-based pagination (pageSize = 5, listener covers all loaded pages)
- Status pipeline: `Pending` → `Preparing` → `Ready` → `Completed`
- Pending order cancellation triggers an atomic wallet refund

### Reviews
- Proof-of-purchase verification — the app queries completed orders before allowing a review
- Star ratings stored per user per product; `RatingService` atomically updates `avgRating`, `ratingCount`, and `ratingDistribution`

### Loyalty Cards
- Loyalty cards with points tracking and shared access across multiple user IDs
- Card management in the Account tab

### Admin Dashboard
- KPI cards: revenue today/week/month, active orders, new customers
- Live order queue with status filter and FCM notifications to customers on status change
- Product management: add, edit, delete, seed sample data (Dev scheme only)
- Sales analytics: revenue over time and peak-hour heatmap
- Review moderation: hide/unhide reviews per product

### Platform
- Push notifications via Firebase Cloud Messaging (FCM) with deep-link routing to Orders tab
- Four-color theme system (Brown, Strawberry, Matcha, Oreo) with light/dark mode, persisted via `@AppStorage`
- Offline detection with a sticky banner when connectivity drops
- Four Xcode schemes pointing to separate Firebase projects (Dev, SIT, UAT, Production)

## Tech Stack

| Area | Technology |
|------|-----------|
| UI | SwiftUI (iOS 17+) |
| Architecture | MVVM + Repository pattern |
| Backend | Firebase Auth, Firestore, Cloud Messaging, Crashlytics, Analytics, Performance |
| Maps | MapKit + CoreLocation |
| Real-time | Firestore snapshot listeners |
| Atomic writes | `db.runTransaction()` for wallet and order mutations |
| Min iOS | 17.0 |

## Architecture

CoffeeCraft follows MVVM with a Repository layer. ViewModels never import Firebase directly — they depend only on repository protocols, making the Firebase implementation swappable without touching any View or ViewModel.

```
View (SwiftUI)
  └─ ViewModel (@MainActor, @Published state)
       └─ Repository Protocol
            └─ Firebase Repository (Firestore / Firebase Auth)
```

Global state is distributed via `@EnvironmentObject` injected at the root:

| Object | Purpose |
|--------|---------|
| `UserSession.shared` | Current user, role, auth state |
| `AuthViewModel` | Sign-in, registration, session restore |
| `OrderViewModel` | Real-time customer orders with pagination |
| `WalletViewModel` | Real-time wallet balance and transactions |
| `ThemeManager.shared` | Appearance mode and color palette |
| `NotificationCoordinator.shared` | Deep-link routing from push taps |

Real-time data strategy:

| Strategy | Used For |
|----------|---------|
| Snapshot listeners | Products, wallet balance, wallet transactions, inbox |
| Cursor-based pagination | Orders |
| `db.runTransaction()` | Wallet top-up, order payment, cancellation refund |

## File Structure

```
CoffeeCraft/
├── Main/
│   └── View/
│       ├── CoffeeCraftApp.swift      # @main entry, EnvironmentObjects injected here
│       ├── RootView.swift            # Auth gate + tab routing
│       ├── TabBarView.swift          # Custom animated tab bar, role-filtered tabs
│       └── AppDelegate.swift         # FCM setup, push notification delegate
│
├── Module/                           # Feature modules
│   ├── Auth/
│   ├── Home/
│   ├── Menu/
│   ├── ProductCustomization/
│   ├── Cart/
│   ├── Order/
│   ├── Wallet/
│   ├── Review/
│   ├── Favorites/
│   ├── Map/
│   ├── Account/
│   ├── AdminDashboard/
│   ├── Notification/
│   ├── Theme/
│   └── Settings/
│
├── Repository/                       # Protocol + Firebase implementations
│   ├── Auth/
│   ├── Product/
│   ├── Order/
│   └── Wallet/
│
├── Custom/                           # 30+ reusable SwiftUI components
│   ├── API_UI_Components/            # AlertManager, ToastManager, LoaderManager, ShimmerView
│   ├── MaterialTextField.swift
│   ├── AsyncImageCard.swift
│   ├── InfiniteCarousel.swift
│   └── ChipFlowLayout.swift
│
├── Extension/
│   ├── Color+Ex.swift                # Semantic color token system
│   ├── Font+Ex.swift
│   └── View+Ex.swift
│
├── Utilize/
│   ├── UserSession.swift
│   ├── AppLog.swift                  # Structured logging
│   ├── AnalyticsService.swift
│   └── Network/NetworkMonitor.swift
│
├── Constants/
│   └── FirebaseKeys.swift            # All Firestore collection/field name constants
│
└── docs/
    ├── firestore-schema.md
    ├── architecture.md
    ├── theme-system.md
    ├── navigation.md
    └── custom-components.md
```

## Highlights

- **Atomic wallet transactions** — every balance mutation uses `db.runTransaction()`, keeping the wallet document and ledger collection in sync even under concurrent writes
- **Proof-of-purchase reviews** — the app queries completed orders before allowing a review submission, preventing fake ratings
- **4-environment Firebase setup** — separate Dev, SIT, UAT, and Production Firebase projects via Xcode schemes, each with its own `GoogleService-Info.plist`
- **Dual-role tab architecture** — `Tab.visible(for:)` filters out the Dashboard tab for customers, so customers see 4 tabs and managers see 5 with no branching in the view hierarchy
- **Token-driven theme system** — semantic color tokens (`Color.accentPrimary`, `Color.bgPrimary`) resolve through `ThemeManager`, so palette swaps re-render the entire UI by changing one `@AppStorage` value

## Screenshots

<p align="center">
  <img src="assets/coffeecraft/screenshot-1.png" width="240"/>
  <img src="assets/coffeecraft/screenshot-2.png" width="240"/>
  <img src="assets/coffeecraft/screenshot-3.png" width="240"/>
</p>

> _Add screenshots to `projects/assets/coffeecraft/` and update the filenames above._

## Links

- [GitHub](https://github.com/cobra-PICH/CoffeeCraft)
