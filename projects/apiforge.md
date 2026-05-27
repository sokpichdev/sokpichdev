# APIForge

> Native multiplatform API client for macOS, iPadOS, and iOS

## Overview

APIForge is a native Apple-platform API client — think Postman, but built entirely in SwiftUI and running natively on Mac, iPad, and iPhone. It lets you craft and send HTTP requests, inspect responses, and manage collections across devices.

## Features

- Build and send HTTP requests (GET, POST, PUT, DELETE, etc.)
- Inspect response headers, body, and status codes
- Manage saved request collections
- Native experience on macOS, iPadOS, and iOS
- Runs fully offline — no account or cloud dependency

## Tech Stack

| Area | Technology |
|------|-----------|
| UI | SwiftUI |
| Concurrency | Swift Concurrency (async/await) |
| Networking | URLSession |
| Platforms | macOS, iPadOS, iOS |

## Highlights

- Single SwiftUI codebase adapts its layout for each platform (Mac sidebar, iPad split view, iPhone stack)
- Swift Concurrency keeps the UI fully responsive during network requests
- No Electron, no web wrapper — entirely native performance

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
