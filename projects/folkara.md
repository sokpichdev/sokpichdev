<h1 align="center">Folkara</h1>

<p align="center">
  <strong>HR & Workflow Management platform for businesses — attendance, approvals, and biometric security, all from a phone</strong><br/>
  <sub>Shipped to the App Store and used by real teams — a production codebase with 500+ merged pull requests.</sub>
</p>

<p align="center">
  <img alt="Platform" src="https://img.shields.io/badge/platform-iOS%2016.4%2B-blue"/>
  <img alt="Language" src="https://img.shields.io/badge/Swift-5-orange"/>
  <img alt="UI" src="https://img.shields.io/badge/UI-SwiftUI-green"/>
  <img alt="Status" src="https://img.shields.io/badge/status-shipped-brightgreen"/>
</p>

<p align="center">
  <a href="https://apps.apple.com/kh/app/folkara/id6745320437">📱 App Store</a>
</p>

---

## Table of Contents

- [Screenshots](#screenshots)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Folder Structure](#folder-structure)
- [Try It](#try-it)
- [Testing](#testing)
- [CI/CD](#cicd)
- [Privacy & Permissions](#privacy--permissions)
- [Accessibility](#accessibility)
- [Project Status](#project-status)
- [Author](#author)

---

## Screenshots

**Onboarding & Authentication**

| Language Selection | Choose Organization | Login | Enter Password | OTP Verification |
|---|---|---|---|---|
| <img src="assets/folkara/choose_language.png" width="160"/> | <img src="assets/folkara/choose_org.png" width="160"/> | <img src="assets/folkara/login.png" width="160"/> | <img src="assets/folkara/password.png" width="160"/> | <img src="assets/folkara/verification_code.png" width="160"/> |

**Home & Attendance**

| Home Dashboard | Today Attendance | Monthly Attendance | Working Days |
|---|---|---|---|
| <img src="assets/folkara/home.png" width="160"/> | <img src="assets/folkara/attendance.png" width="160"/> | <img src="assets/folkara/monthly_attendance.png" width="160"/> | <img src="assets/folkara/working_days.png" width="160"/> |

**Approval & Requests**

| Request List | Submit Request | Create Request Form |
|---|---|---|
| <img src="assets/folkara/request.png" width="160"/> | <img src="assets/folkara/submit_request.png" width="160"/> | <img src="assets/folkara/create_form.png" width="160"/> |

| Request Detail — CC | Request Detail — Comment | Comments List | Add Comment |
|---|---|---|---|
| <img src="assets/folkara/request_detail_cc_copy.png" width="160"/> | <img src="assets/folkara/request_detail_ccd_record_comment.png" width="160"/> | <img src="assets/folkara/comments_list.png" width="160"/> | <img src="assets/folkara/add_cmt.png" width="160"/> |

**Profile & Documents**

| Profile | Personal Details | Employment Details | Document Details | Work History |
|---|---|---|---|---|
| <img src="assets/folkara/profile.png" width="160"/> | <img src="assets/folkara/personal_details.png" width="160"/> | <img src="assets/folkara/employment_details.png" width="160"/> | <img src="assets/folkara/docs_details.png" width="160"/> | <img src="assets/folkara/work_history.png" width="160"/> |

**Devices, Assets & Notifications**

| Linked Devices | Scan QR Code | Assets | Upcoming Birthdays | Notifications |
|---|---|---|---|---|
| <img src="assets/folkara/devices.png" width="160"/> | <img src="assets/folkara/scan_qr_code.png" width="160"/> | <img src="assets/folkara/assets.png" width="160"/> | <img src="assets/folkara/upcoming_bd.png" width="160"/> | <img src="assets/folkara/notification.png" width="160"/> |

**Organization**

| Switch Organization |
|---|
| <img src="assets/folkara/switch_org.png" width="160"/> |

---

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

---

## Tech Stack

| Layer | Choice |
|---|---|
| **Language** | Swift 5 |
| **UI** | SwiftUI (primary), UIKit interop where needed |
| **Architecture** | MVVM (Model / View / ViewModel) |
| **Networking** | URLSession-based `RestAPI` REST layer |
| **Persistence** | Keychain (auth token), `UserDefaults` (preferences) |
| **Backend / BaaS** | Firebase (Analytics, App Check, Cloud Messaging) |
| **Dependencies** | Swift Package Manager — SDWebImageSwiftUI, swiftui-introspect, firebase-ios-sdk, DeviceKit |
| **CI/CD** | Fastlane |
| **Linting** | SwiftLint |
| **Min iOS** | 16.4+ |

---

## Architecture

The app is SwiftUI-first (171 of 210 Swift files) and follows MVVM throughout. The entry point uses a `UIApplicationDelegateAdaptor` to bridge `AppDelegate` for Firebase and push-notification setup, and drives top-level navigation from `@AppStorage`-backed state:

```
isFirstLaunch → Language selection (onboarding)
token empty   → Login
biometric on  → Enter password (Face ID / Touch ID gate)
otherwise     → Main app (Tab bar)
```

```mermaid
graph TD
    Views["Module Views (Auth / Attendance / Approval / Profile)"] --> ViewModels["ViewModels"]
    ViewModels --> RestAPI["RestAPI (URLSession)"]
    ViewModels --> Keychain["Keychain (session token)"]
    RestAPI --> API["Loma Technology API"]
    ViewModels --> Firebase["Firebase (Analytics, App Check, FCM)"]
```

**Key decisions**
- Each feature module under `Modules/` owns its own Model / View / ViewModel — no shared cross-feature state beyond the `Common/` services layer.
- Approval request forms are formula-driven: field visibility and validation are resolved from server-supplied form definitions at runtime, not hardcoded per request type.
- A shared `Common/CustomView` library (~25 components) is reused across every module rather than duplicating UI per feature.

**Full app flow — launch to core modules**

```mermaid
flowchart TD
    Start(["App Launch"]) --> FirstLaunch{"First launch?"}
    FirstLaunch -- Yes --> LangSelect["Language Selection\n(OnBoarding)"]
    LangSelect --> Onboarding["Onboarding Screens"]
    Onboarding --> TokenCheck
    FirstLaunch -- No --> TokenCheck{"Session token stored?"}

    TokenCheck -- No --> JoinOrg["Join Organization"]
    JoinOrg --> Login["Login\n(email / phone)"]
    Login --> OTP["OTP Verification"]
    OTP --> PolicyTerm["Policy & Terms Acceptance"]
    PolicyTerm --> TokenIssued(["Token issued & stored in Keychain"])
    Login -.->|Forgot password| ForgotPassword["Forgot / Reset Password"]
    ForgotPassword --> Login

    TokenCheck -- Yes --> BiometricCheck{"Biometric lock enabled?"}
    BiometricCheck -- Yes --> EnterPassword["Enter Password\n(Face ID / Touch ID gate)"]
    EnterPassword --> MainApp
    BiometricCheck -- No --> MainApp
    TokenIssued --> MainApp["Main App (Tab Bar)"]

    MainApp --> Home["Home Dashboard"]
    MainApp --> Attendance["Attendance"]
    MainApp --> Approval["Approval"]
    MainApp --> Notification["Notifications"]
    MainApp --> ProfileMenu["Profile Menu"]

    Attendance --> TodayAttendance["Today Attendance\n(check-in / check-out)"]
    Attendance --> MonthlyAttendance["Monthly Attendance Overview"]
    Attendance --> LeaveDetail["Leave Detail"]

    Approval --> ToDo["To-Do List"]
    Approval --> RaiseNewRequest["Raise New Request\n(dynamic form)"]
    ToDo --> WorkFlow["Workflow"]
    WorkFlow --> WorkFlowDetail["Workflow Detail"]
    WorkFlowDetail --> Comment["Comments Thread"]
    RaiseNewRequest --> ToDo

    ProfileMenu --> Profile["Profile"]
    ProfileMenu --> ProfileInfo["Profile Info"]
    ProfileMenu --> LinkedDevices["Linked Devices"]
    ProfileMenu --> Setting["Settings\n(dark mode, language)"]
    ProfileMenu --> Scheme["Scheme"]
    Setting -.->|Switch organization| JoinOrg
    Profile -.->|Logout| TokenCheck
```

---

## Folder Structure

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

**Reusable component library** — `Common/CustomView` houses ~25 shared UI components, including `ShimmerView` (loading skeletons), `ToastView`, `LoadingView`, `NoConnectionView`, `NoDataView`, `MediaPicker`, `DynamicTextEditor` (UIKit + SwiftUI variants), `MentionHTMLText`, `CustomNavigation`, `CustomProfileImageView`, `TableView`, and `YearMonthPickerView`.

---

## Try It

Folkara is shipped and live on the App Store — the fastest way to see it is to install it, not build it locally.

<p align="center">
  <a href="https://apps.apple.com/kh/app/folkara/id6745320437">📱 Get it on the App Store</a>
</p>

---

## Testing

No test coverage information was available to verify — **TODO**.

---

## CI/CD

Fastlane is configured (`fastlane/Fastfile`, `Appfile`, `Gemfile`) for build and release automation to TestFlight / App Store Connect.

---

## Privacy & Permissions

- **Biometrics (Face ID / Touch ID):** used to gate app re-entry after login.
- **Push notifications:** used for workflow/approval alerts via Firebase Cloud Messaging.
- **Data collected:** not published — **TODO**.
- **Third parties:** Firebase (Analytics, App Check, Cloud Messaging).

---

## Accessibility

Not formally audited — **TODO**.

---

## Project Status

✅ Shipped to the App Store and in active use by real teams — attendance, approvals, biometric login, and multi-language support are all live in production.

---

## Author

**Sok Pich** — [@sokpichdev](https://github.com/sokpichdev)
<sub>Contributed as part of a multi-engineer team at Loma Technology (Cambodia); not the sole author of this codebase.</sub>
