# Folkara

> Human Resource & Workflow Management app — available on the App Store

## Overview

Folkara is a production iOS app that streamlines HR and workflows management for businesses. Employees check in and out, submit and track leave requests, and route them through multi-step approval workflows, while managers review and act on the requests assigned to them — all from their phone, in their preferred language. Built as professional work at Loma Technology (Cambodia).

## Features

### Authentication & Security
- Organization-based login (join an organization, then sign in)
- OTP verification and forgot/reset password flows
- Biometric authentication (Face ID / Touch ID) with passcode fallback
- Token-based session management
- Policy & Terms acceptance and linked-device management

### Attendance
- Daily check-in / check-out
- Monthly attendance overview
- Leave detail views

### Approval Workflows
- Raise new requests via dynamic, formula-driven forms
- To-Do list of requests awaiting the user's action
- Multi-step workflows with full detail views
- Threaded comments on requests

### Other
- Home dashboard
- Push notifications (Firebase Cloud Messaging)
- Profile & profile-info management
- Settings with dark mode and color scheme options
- Multi-language support via a custom in-app localization system
- Onboarding flow for first launch
- Offline detection with a dedicated no-connection state

## Tech Stack

| Area | Technology |
|------|-----------|
| UI | SwiftUI (primary) with UIKit interop where needed |
| Architecture | MVVM (Model / View / ViewModel) |
| Min iOS | 16.4+ |
| Backend services | Firebase (Analytics, App Check, Messaging) |
| Networking | URLSession-based REST layer |
| Images | SDWebImage / SDWebImageSwiftUI |
| Utilities | DeviceKit, SwiftUI-Introspect |
| Connectivity | Custom NetworkMonitor / Reachability |
| CI/CD | Fastlane |
| Linting | SwiftLint |

## Architecture

The app is SwiftUI-first (171 of 210 Swift files) and follows MVVM throughout. The entry point uses a `UIApplicationDelegateAdaptor` to bridge `AppDelegate` for Firebase and push-notification setup, and drives top-level navigation from `@AppStorage`-backed state:

```
isFirstLaunch → Language selection (onboarding)
token empty   → Login
biometric on  → Enter password (Face ID / Touch ID gate)
otherwise     → Main app (Tab bar)
```

## File Structure

```
LMS-iOS/
├── MainApp/          # App entry, AppDelegate
├── Modules/
│   ├── Language/     # In-app language selection (MVVM)
│   ├── OnBoarding/
│   ├── Authentication/  # Login, OTP, Password, ForgotPassword,
│   │                    # JoinOrganization, PolicyTerm, EnterPassword
│   └── Main/
│       ├── Home/
│       ├── Attendance/   # TodayAttendance, MonthlyAttendance, LeaveDetail
│       ├── Approval/     # RaiseNewRequest, ToDo, WorkFlow,
│       │                 # WorkFlowDetail, Comment
│       ├── Notification/
│       ├── ProfileMenu/  # Profile, ProfileInfo, LinkedDevices,
│       │                 # Setting, Scheme
│       └── Tabbar/
├── Common/
│   ├── APIManager/   # RestAPI, APIResource, BaseModel, ConfigurationDataManager
│   ├── CustomView/   # ~25 reusable components
│   ├── Extension/    # Swift/SwiftUI extensions
│   ├── NetworkMonitor/
│   ├── Constant/     # Constants, LocalizeConstant, AppLogger
│   └── Utilize/      # Helpers
└── Resources/        # Assets, Fonts, Firebase config
```

### Reusable component library
`Common/CustomView` houses ~25 shared UI components, including `ShimmerView` (loading skeletons), `ToastView`, `LoadingView`, `NoConnectionView`, `NoDataView`, `MediaPicker`, `DynamicTextEditor` (UIKit + SwiftUI variants), `MentionHTMLText`, `CustomNavigation`, `CustomProfileImageView`, `TableView`, and `YearMonthPickerView`.

## Highlights

- Shipped to the App Store and used by real teams
- Production codebase with 500+ merged pull requests across a team — a real collaborative, long-lived project
- SwiftUI-first architecture with a clean MVVM module structure
- Dynamic, formula-driven request forms that resolve field values at runtime
- Substantial in-house component library reused across the app

## Screenshots

<p align="center">
  <img src="assets/folkara/screenshot-1.png" width="240"/>
  <img src="assets/folkara/screenshot-2.png" width="240"/>
  <img src="assets/folkara/screenshot-3.png" width="240"/>
</p>
## Links

- [App Store](https://apps.apple.com/kh/app/folkara/id6745320437)
