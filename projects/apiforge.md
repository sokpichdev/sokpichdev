# APIForge

> Native multiplatform API client for macOS, iPadOS, and iOS

## Overview

APIForge is a native Apple-platform API client — think Postman, but built entirely in SwiftUI and running natively on Mac, iPad, and iPhone. It runs fully offline, requires no account, and stores everything as human-readable JSON files you can check into version control.

## Features

### Requests
- HTTP methods: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS
- Query params, headers, and body editors (raw, JSON, form-urlencoded, multipart with file parts)
- Auth tab (basic / bearer)
- Inline editable request name and resolved-URL preview with unresolved-variable hints
- Keyboard shortcuts: `⌘⏎` to send, `⌘N` for a new request

### Collections & History
- Collections and folders saved as JSON files (git-friendly)
- Sidebar with collapsible collections, request count badges, rename / duplicate / delete
- Request history (last 200) with tap-to-load, swipe-to-delete, clear-all, and "Add to Collection"

### Environments & Variables
- Multiple environments with editable key/value rows
- `{{variable}}` substitution across URL, headers, params, and body
- Environment picker in the main toolbar

### Import / Export
- Paste-cURL detection with import banner
- Postman v2.1 collection import and export
- Copy any request as cURL

### Polish
- Toasts for send / import / export success and errors
- Empty states and keyboard shortcuts throughout

## Tech Stack

| Area | Technology |
|------|-----------|
| UI | SwiftUI |
| Concurrency | Swift Concurrency (async/await) |
| Networking | URLSession |
| Persistence | JSON files (Application Support directory) |
| Testing | Swift Testing |
| Platforms | macOS 14+, iPadOS 17+, iOS 17+ |

## Highlights

- Single SwiftUI codebase adapts its layout for each platform (Mac sidebar, iPad split view, iPhone stack)
- Fully offline — no account, no cloud sync, no telemetry
- Git-friendly JSON storage: collections, environments, and history are all human-readable files
- Postman-compatible: import and export Postman v2.1 collections to interoperate with existing workflows
- Swift Concurrency keeps the UI responsive during network requests — no Electron, no web wrapper

## Screenshots

<p align="center">
  <img src="assets/apiforge/screenshot-mac.png" width="160"/>
</p>
<p align="center">
  <img src="assets/apiforge/screenshot-ipad.png" width="160"/>
  <img src="assets/apiforge/screenshot-iphone.png" width="160"/>
</p>

> _Add screenshots to `projects/assets/apiforge/` and update the filenames above (Mac/iPad/iPhone views show off the multiplatform layout)._

## Links

- [GitHub](https://github.com/cobra-PICH/APIForge)
