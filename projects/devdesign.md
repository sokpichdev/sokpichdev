# DevDesign

> Offline-first iOS toolkit for designers and developers — 17 tools, ~741 tests, AI-powered palettes

## Overview

DevDesign is a native iPhone app for iOS 17+ that bundles 17 reference and generation tools for designers and developers — color palettes, typography, spacing, gradients, shadows, component snippets, layout tools, asset generators, and AI-powered palette generation — all working without a network connection (except the optional AI feature). No backend, no ads, no account required.

## Features

### Color Tools
- Palette Generator: complementary, triadic, analogous, split-complementary, and tetradic harmonies
- Color Picker with HEX / RGB / HSB values and SwiftUI code export
- Contrast Checker with WCAG AA & AAA compliance and suggested passing colors
- Saved Palettes persisted via SwiftData with CloudKit sync

### Typography & Spacing
- Type Scale Generator with 8 modular-scale ratio presets
- Font Pairing combining Google Fonts and system fonts with live preview
- Spacing System: 4pt grid visualizer with a comparison tool
- SF Symbols Browser with search, category filter, and copy-as-SwiftUI

### Components & Layout
- Shadow Playground: multi-layer shadow builder with code export
- Gradient Builder: linear and radial gradient editor
- Component Snippets: ~80 SwiftUI snippets across 10 categories with `{{ACCENT}}` token substitution
- Layout Inspector: safe area, padding playground, and device presets

### Assets & Motion
- App Icon Generator: all 14 iOS sizes, `Contents.json`, and PNG export
- Animation Playground: spring & easing curve builder with 6 live preview targets
- Border & Decoration: corners, borders, glows, and overlay patterns
- Design Token Exporter: Swift enum, W3C JSON, and CSS custom properties

### AI Palette
- Text-prompt palette generation via Claude (Sonnet 4.5), Gemini (2.5 Flash), or OpenRouter (free Llama 3.3 70B)
- OpenRouter is the default — users generate immediately with no setup
- Structured JSON schema with name, mood, roles, and usage hints per color
- Prompt suggestion library (25 suggestions across 5 categories) and prompt history with palette snapshots
- Staggered spring color-reveal animation; save directly to Saved Palettes

## Tech Stack

| Area | Technology |
|------|-----------|
| UI | SwiftUI (iOS 17+) |
| State | `@Observable` macro (Swift 5.9) |
| Architecture | MVVM + Feature Modules |
| Persistence | SwiftData |
| Sync | CloudKit |
| Networking | URLSession (AI Palette only) |
| AI Providers | Anthropic, Google Gemini, OpenRouter |
| Font Loading | CoreText with actor-based loader and request coalescing |
| Image Export | `ImageRenderer` for app icons and shareable assets |
| Min iOS | 17.0 |
| Device | iPhone only |
| Dependencies | None (zero SPM packages) |

## Architecture

DevDesign follows MVVM with strict feature isolation — every feature owns its own `View`, `ViewModel`, and tests folder under `Features/`. There is no shared mega-ViewModel and no tab bar; a single dashboard grid in `ContentView` routes to each feature.

```
View (SwiftUI)
  └─ ViewModel (@Observable)
       └─ Core Services (HarmonyEngine, ContrastEngine, ExportService)
            └─ SwiftData / CloudKit (SavedPalette, SavedColor)
```

Core engineering patterns:

| Pattern | Purpose |
|---------|---------|
| `@Observable` struct-array copy-mutate-reassign | Ensures SwiftUI detects struct mutations inside observable arrays |
| `forceSyncTrigger: Int` counter | Forces downstream UI sync after programmatic state changes |
| `updateInPlace()` vs `regenerate()` | Smooth in-place animations vs explicit fresh-result insertions |
| `onUpdate: ((inout T) -> Void) -> Void` | Avoids `Binding` trailing-closure ambiguity in row components |
| Extracted `ColorPicker` bindings | Avoids SwiftUI `ColorPicker` trailing-closure ambiguity |
| Side-effect-free `AppIconCanvasView` | Renders identically as a live preview and as an `ImageRenderer` source |

## File Structure

```
DevDesign/
├── App/
│   ├── DevDesignApp.swift          # @main entry, SwiftData container setup
│   └── ContentView.swift           # Dashboard grid routing to every feature
│
├── Core/
│   ├── Models/
│   │   ├── DevColor.swift          # Core color model (HSB/RGB/HEX)
│   │   ├── SavedPalette.swift      # SwiftData model
│   │   └── SavedColor.swift        # SwiftData model
│   ├── Extensions/
│   │   ├── Color+Hex.swift
│   │   ├── Color+Harmony.swift     # Complementary / triadic / analogous
│   │   └── Color+Contrast.swift    # WCAG luminance & ratio
│   └── Services/
│       ├── HarmonyEngine.swift     # Palette harmony algorithms
│       ├── ContrastEngine.swift    # WCAG AA/AAA calculations
│       └── ExportService.swift     # HEX/RGB/SwiftUI code strings
│
├── Features/                       # One folder per tool
│   ├── Dashboard/
│   ├── PaletteGenerator/
│   ├── ColorPicker/
│   ├── ContrastChecker/
│   ├── SavedPalettes/
│   ├── TypeScale/
│   ├── FontPairing/
│   ├── SpacingSystem/
│   ├── SFSymbols/
│   ├── ShadowPlayground/
│   ├── GradientBuilder/
│   ├── ComponentSnippets/
│   ├── LayoutInspector/
│   ├── AppIconGenerator/
│   ├── AnimationPlayground/
│   ├── BorderDecoration/
│   ├── DesignTokenExporter/
│   └── AIPalette/
│       ├── Models/
│       ├── Networking/             # One API types file per provider
│       ├── Errors/
│       ├── Providers/
│       ├── Services/
│       ├── ViewModels/
│       └── Views/
│
├── DesignSystem/
│   ├── DSColors.swift              # Semantic color tokens
│   ├── DSTypography.swift          # Type scale tokens
│   └── DSSpacing.swift             # Spacing & radius tokens
│
├── Shared/                         # Reusable views used across features
└── DevDesignTests/                 # ~741 unit tests across 18 files
```

## Highlights

- **17 tools in one app, fully offline** — only the AI Palette feature touches the network; everything else works on a plane
- **Multi-provider AI generation** — Claude, Gemini, and OpenRouter behind a single `AIProvider` protocol, with OpenRouter as a zero-setup free default
- **Schema-constrained AI output** — the system prompt locks the model to a strict JSON schema (name, mood, hex, role, usage), with a recovery attempt on malformed responses
- **Zero external dependencies** — no SPM packages, no third-party SDKs; everything built on Apple frameworks
- **~741 unit tests** across 18 feature files covering harmony algorithms, WCAG contrast math, ViewModel state transitions, and export string generation
- **Design Token Exporter** emits Swift enums, W3C JSON, and CSS custom properties from your live SwiftData palettes
- **`@Observable` + SwiftData + CloudKit** — modern Swift 5.9 stack with no `ObservableObject` legacy

## Screenshots

<p align="center">
  <img src="assets/devdesign/screenshot-1.png" width="160"/>
  <img src="assets/devdesign/screenshot-2.png" width="160"/>
  <img src="assets/devdesign/screenshot-3.png" width="160"/>
</p>

> _Add screenshots to `projects/assets/devdesign/` and update the filenames above._

## Links

- [GitHub](https://github.com/cobra-PICH/DevDesign)
