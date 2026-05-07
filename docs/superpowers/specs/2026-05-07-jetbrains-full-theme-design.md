# JetBrains Full UI Theme — Design Spec

**Date:** 2026-05-07
**Project:** Electronic Moonlight Theme
**Scope:** Convert the existing JetBrains color scheme plugin into a full IDE UI theme for Rider (and all JetBrains IDEs)

---

## Goal

The current plugin only registers an editor color scheme, which appears under Settings → Editor → Color Scheme. The goal is a full UI theme that appears under Settings → Appearance → Theme — covering the entire IDE chrome: sidebar, tabs, toolbar, status bar, menus, buttons, dialogs, and the editor together in one cohesive look.

---

## Color Palette

All colors are derived from the existing Electronic Moonlight palette.

| Role | Color | Usage |
|---|---|---|
| Editor background | `#1D1F31` | Editor pane, active tab background |
| Chrome background | `#1E2030` | Sidebar, toolbar, tabs bar, status bar |
| Sidebar background | `#1E2032` | Project tree panel |
| Primary text | `#C8D3F5` | Default foreground, active tab text |
| Muted text | `#828BB8` | Inactive labels, status bar text, line numbers |
| Borders / separators | `#2A2D3D` | Panel borders, tab dividers |
| Selected / active item | `#2A2D4A` | Highlighted tree node, selected list item |
| Accent | `#C099FF` | Buttons, active tab indicator, links, focus rings, checkboxes |
| Error | `#FF757F` | Error highlights, red squiggles |
| Warning | `#FFC777` | Warning highlights |
| Success / info | `#C3E88D` | Success indicators |
| Caret | `#F30F4C` | Editor cursor |

---

## Architecture

### New file: `themes/Electronic Moonlight.theme.json`

A JetBrains theme descriptor. Top-level keys:

- `"name"`: `"Electronic Moonlight"`
- `"dark"`: `true`
- `"author"`: `"Isaac Arnold"`
- `"editorScheme"`: `"/colors/Electronic Moonlight.icls"` — links the existing editor color scheme so both are applied together
- `"colors"`: named color variables that can be referenced in the `"ui"` section
- `"ui"`: maps JetBrains UI keys to colors — this is the bulk of the file

### Updated file: `META-INF/plugin.xml`

Replace the `bundledColorScheme` extension with a `themeProvider` extension:

```xml
<extensions defaultExtensionNs="com.intellij">
  <themeProvider id="com.electronicmoonlight.theme"
                 path="/themes/Electronic Moonlight.theme.json"/>
</extensions>
```

The `themeProvider` registers the theme in the Appearance dropdown. Because `editorScheme` is set in the JSON, the `.icls` is bundled implicitly — the separate `bundledColorScheme` entry is no longer needed and should be removed.

### Unchanged file: `colors/Electronic Moonlight.icls`

No changes required. The theme JSON references it as-is.

### Resource layout after change

```
jetbrains-plugin/src/main/resources/
  META-INF/
    plugin.xml
  themes/
    Electronic Moonlight.theme.json   ← new
  colors/
    Electronic Moonlight.icls         ← unchanged
```

---

## UI Sections to Theme

The `"ui"` block in the theme JSON must cover:

| Area | Key examples |
|---|---|
| General / defaults | `*.background`, `*.foreground`, `*.selectionBackground`, `*.selectionForeground` |
| Editor tabs | `EditorTabs.background`, `EditorTabs.underlinedTabBackground`, `EditorTabs.underlineColor`, `EditorTabs.inactiveUnderlineColor` |
| Tool window / panels | `ToolWindow.background`, `ToolWindow.Header.background`, `ToolWindow.Header.foreground` |
| Project tree | `Tree.background`, `Tree.foreground`, `Tree.selectionBackground`, `Tree.selectionForeground` |
| Toolbar | `MainToolbar.background`, `MainToolbar.foreground` |
| Status bar | `StatusBar.background`, `StatusBar.foreground`, `StatusBar.borderColor` |
| Menus | `Menu.background`, `Menu.foreground`, `Menu.selectionBackground`, `MenuItem.selectionBackground` |
| Buttons | `Button.background`, `Button.foreground`, `Button.default.background` (accent), `Button.default.foreground` |
| Input fields | `TextField.background`, `TextField.foreground`, `TextField.caretForeground`, `Component.focusedBorderColor` (accent) |
| Scrollbars | `ScrollBar.background`, `ScrollBar.thumb.background`, `ScrollBar.thumb.hoverBackground` |
| Popups / dialogs | `Popup.background`, `Popup.borderColor` |
| Notifications | `Notification.background`, `Notification.errorBackground` |
| Checkboxes / toggles | `Checkbox.select.background` (accent) |
| Links | `Link.activeForeground`, `Link.hoverForeground` (accent) |
| Run / debug console | Inherits from `.icls` console colors |

---

## Build

No changes to `build.gradle.kts` are needed. Gradle picks up everything under `src/main/resources/` automatically. The new `themes/` directory is just another resource folder.

---

## Success Criteria

1. After installing the built ZIP in Rider, "Electronic Moonlight" appears in Settings → Appearance → Theme (not just Color Scheme).
2. Selecting the theme changes both the IDE chrome and the editor colors simultaneously.
3. The accent color (`#C099FF` purple) is visible on active tab indicators, primary buttons, and focused input borders.
4. No visible color mismatches between the editor pane and surrounding chrome.
