# JetBrains Full UI Theme Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the existing JetBrains color scheme plugin into a full IDE UI theme that appears in Settings → Appearance → Theme and styles the entire IDE chrome.

**Architecture:** Add a `Electronic Moonlight.theme.json` file that maps JetBrains UI keys to the Electronic Moonlight palette, then update `plugin.xml` to register it via `themeProvider` (replacing the existing `bundledColorScheme` entry). The theme JSON references the existing `.icls` via `editorScheme` so editor and chrome are applied together.

**Tech Stack:** JetBrains theme JSON format, Gradle (Java 17 toolchain)

---

### Task 1: Create the theme JSON file

**Files:**
- Create: `jetbrains-plugin/src/main/resources/themes/Electronic Moonlight.theme.json`

- [ ] **Step 1: Create the themes directory and write the theme file**

```bash
mkdir -p jetbrains-plugin/src/main/resources/themes
```

Then create `jetbrains-plugin/src/main/resources/themes/Electronic Moonlight.theme.json` with this content:

```json
{
  "name": "Electronic Moonlight",
  "dark": true,
  "author": "Isaac Arnold",
  "editorScheme": "/colors/Electronic Moonlight.icls",

  "colors": {
    "background":         "#1D1F31",
    "chrome":             "#1E2030",
    "sidebar":            "#1E2032",
    "text":               "#C8D3F5",
    "textMuted":          "#828BB8",
    "border":             "#2A2D3D",
    "selection":          "#2A2D4A",
    "selectionInactive":  "#232538",
    "hover":              "#252840",
    "accent":             "#C099FF",
    "accentHover":        "#CEB3FF",
    "accentDim":          "#9B7AFF",
    "accentFg":           "#1D1F31",
    "error":              "#FF757F",
    "errorBg":            "#3D1E24",
    "warning":            "#FFC777",
    "warningBg":          "#3D2E14",
    "success":            "#C3E88D",
    "caret":              "#F30F4C",
    "scrollThumb":        "#3A3D52",
    "scrollThumbHover":   "#4A4D62",
    "inputBg":            "#1D1F31",
    "popupBg":            "#1B1D2C",
    "stripeBg":           "#1A1C2E",
    "buttonBg":           "#252840",
    "buttonBorder":       "#3A3D52"
  },

  "ui": {
    "*": {
      "background":             "chrome",
      "foreground":             "text",
      "selectionBackground":    "selection",
      "selectionForeground":    "text",
      "disabledBackground":     "stripeBg",
      "disabledForeground":     "textMuted",
      "inactiveBackground":     "chrome",
      "inactiveForeground":     "textMuted",
      "borderColor":            "border",
      "separatorColor":         "border"
    },

    "ActionButton": {
      "hoverBackground":        "hover",
      "hoverBorderColor":       "border",
      "pressedBackground":      "selection",
      "pressedBorderColor":     "border"
    },

    "Button": {
      "background":             "buttonBg",
      "foreground":             "text",
      "borderColor":            "buttonBorder",
      "hoverBackground":        "selection",
      "default.background":     "accent",
      "default.foreground":     "accentFg",
      "default.borderColor":    "accent",
      "default.hoverBackground":"accentHover",
      "default.startBackground":"accent",
      "default.endBackground":  "accent"
    },

    "Checkbox": {
      "Background.Default":     "inputBg",
      "Background.Default.Dark":"inputBg",
      "Border.Default":         "border",
      "Border.Default.Dark":    "border",
      "Background.Selected":    "accent",
      "Background.Selected.Dark":"accent",
      "Border.Selected":        "accent",
      "Border.Selected.Dark":   "accent",
      "Foreground.Selected":    "accentFg",
      "Foreground.Selected.Dark":"accentFg",
      "Focus.Thin.Default":     "accent",
      "Focus.Thin.Default.Dark":"accent",
      "Focus.Wide":             "accent",
      "Focus.Wide.Dark":        "accent"
    },

    "ComboBox": {
      "background":             "inputBg",
      "foreground":             "text",
      "selectionBackground":    "selection",
      "selectionForeground":    "text",
      "nonEditableBackground":  "inputBg",
      "ArrowButton.background": "inputBg",
      "ArrowButton.iconColor":  "textMuted"
    },

    "Component": {
      "borderColor":            "border",
      "disabledBorderColor":    "border",
      "focusedBorderColor":     "accent",
      "errorFocusColor":        "error",
      "warningFocusColor":      "warning",
      "infoFocusColor":         "accent"
    },

    "Counter": {
      "background":             "accent",
      "foreground":             "accentFg"
    },

    "Debugger": {
      "Variables.backgroundColor": "background"
    },

    "DefaultTabs": {
      "background":             "chrome",
      "underlineColor":         "accent",
      "inactiveUnderlineColor": "border",
      "hoverBackground":        "hover"
    },

    "DragAndDrop": {
      "areaBackground":         "hover",
      "areaForeground":         "text",
      "areaBorderColor":        "accent"
    },

    "EditorTabs": {
      "background":             "chrome",
      "foreground":             "textMuted",
      "selectedBackground":     "background",
      "selectedForeground":     "text",
      "underlinedTabBackground":"background",
      "underlineColor":         "accent",
      "inactiveUnderlineColor": "border",
      "hoverBackground":        "hover",
      "hoverColor":             "text",
      "borderColor":            "border",
      "inactiveColoredFileBackground": "chrome"
    },

    "FileColor": {
      "Yellow":                 "#2E2B1A",
      "Green":                  "#1A2E1A",
      "Blue":                   "#1A1E30",
      "Violet":                 "#251A30",
      "Orange":                 "#2E2018",
      "Rose":                   "#2E1A1E"
    },

    "Link": {
      "activeForeground":       "accent",
      "hoverForeground":        "accentHover",
      "visitedForeground":      "accentDim",
      "pressedForeground":      "accent"
    },

    "List": {
      "background":             "chrome",
      "foreground":             "text",
      "selectionBackground":    "selection",
      "selectionForeground":    "text",
      "selectionInactiveBackground": "selectionInactive",
      "hoverBackground":        "hover"
    },

    "MainToolbar": {
      "background":             "chrome",
      "foreground":             "textMuted",
      "Dropdown.background":    "chrome",
      "Dropdown.hoverBackground":"hover",
      "Icon.hoverBackground":   "hover"
    },

    "Menu": {
      "background":             "popupBg",
      "foreground":             "text",
      "separatorColor":         "border",
      "borderColor":            "border"
    },

    "MenuBar": {
      "background":             "chrome",
      "foreground":             "text",
      "selectionBackground":    "selection",
      "selectionForeground":    "text"
    },

    "MenuItem": {
      "selectionBackground":    "selection",
      "selectionForeground":    "text"
    },

    "NavBar": {
      "background":             "chrome",
      "foreground":             "textMuted"
    },

    "Notification": {
      "background":             "chrome",
      "foreground":             "text",
      "borderColor":            "border",
      "errorBackground":        "errorBg",
      "errorForeground":        "error",
      "errorBorderColor":       "error",
      "warningBackground":      "warningBg",
      "warningForeground":      "warning",
      "warningBorderColor":     "warning",
      "MoreButton.foreground":  "accent",
      "MoreButton.innerBorderColor": "accent"
    },

    "PasswordField": {
      "background":             "inputBg",
      "foreground":             "text",
      "caretForeground":        "caret",
      "borderColor":            "border"
    },

    "Plugins": {
      "background":             "chrome",
      "SearchField.background": "inputBg",
      "SectionHeader.foreground": "textMuted",
      "tagBackground":          "selection",
      "tagForeground":          "text",
      "Button.installBackground":  "accent",
      "Button.installForeground":  "accentFg",
      "Button.installBorderColor": "accent"
    },

    "Popup": {
      "background":             "popupBg",
      "foreground":             "text",
      "borderColor":            "border",
      "separatorColor":         "border",
      "Header.activeBackground":"hover",
      "Header.inactiveBackground": "popupBg",
      "Toolbar.background":     "popupBg",
      "Toolbar.borderColor":    "border"
    },

    "ProgressBar": {
      "background":             "border",
      "foreground":             "accent",
      "progressColor":          "accent",
      "indeterminateStartColor":"accent",
      "indeterminateEndColor":  "accentDim",
      "failedColor":            "error",
      "failedEndColor":         "errorBg",
      "passedColor":            "success",
      "passedEndColor":         "success"
    },

    "RunWidget": {
      "background":             "hover",
      "foreground":             "text",
      "runningBackground":      "hover",
      "stoppedBackground":      "chrome"
    },

    "ScrollBar": {
      "background":             "chrome",
      "thumb.background":       "scrollThumb",
      "thumb.hoverBackground":  "scrollThumbHover",
      "track.background":       "chrome",
      "Transparent.background": "chrome",
      "Transparent.thumb.background":       "scrollThumb",
      "Transparent.thumb.hoverBackground":  "scrollThumbHover"
    },

    "SearchEverywhere": {
      "background":             "popupBg",
      "foreground":             "text",
      "SearchField.background": "inputBg",
      "SearchField.borderColor":"border",
      "Tab.selectedBackground": "selection",
      "Tab.selectedForeground": "text"
    },

    "SearchMatch": {
      "startBackground":        "#2A3A20",
      "endBackground":          "#2A3A20"
    },

    "Separator": {
      "separatorColor":         "border"
    },

    "SidePanel": {
      "background":             "sidebar"
    },

    "SpeedSearch": {
      "background":             "popupBg",
      "foreground":             "text",
      "borderColor":            "accent",
      "errorBackground":        "errorBg",
      "errorForeground":        "error"
    },

    "Spinner": {
      "background":             "inputBg",
      "foreground":             "text",
      "borderColor":            "border"
    },

    "StatusBar": {
      "background":             "chrome",
      "foreground":             "textMuted",
      "borderColor":            "border",
      "hoverBackground":        "hover"
    },

    "TabbedPane": {
      "background":             "chrome",
      "foreground":             "textMuted",
      "selectedForeground":     "text",
      "underlineColor":         "accent",
      "contentAreaColor":       "border",
      "hoverColor":             "hover"
    },

    "Table": {
      "background":             "chrome",
      "foreground":             "text",
      "gridColor":              "border",
      "selectionBackground":    "selection",
      "selectionForeground":    "text",
      "stripeColor":            "stripeBg",
      "sortIconColor":          "textMuted"
    },

    "TextArea": {
      "background":             "inputBg",
      "foreground":             "text",
      "caretForeground":        "caret",
      "selectionBackground":    "selection",
      "selectionForeground":    "text"
    },

    "TextField": {
      "background":             "inputBg",
      "foreground":             "text",
      "caretForeground":        "caret",
      "selectionBackground":    "selection",
      "selectionForeground":    "text",
      "borderColor":            "border"
    },

    "ToggleButton": {
      "onBackground":           "accent",
      "onForeground":           "accentFg",
      "offBackground":          "buttonBg",
      "offForeground":          "textMuted",
      "buttonColor":            "accentFg",
      "borderColor":            "border"
    },

    "Toolbar": {
      "background":             "chrome",
      "borderColor":            "border",
      "Floating.background":    "popupBg"
    },

    "ToolWindow": {
      "background":             "sidebar",
      "foreground":             "text",
      "Header.background":      "chrome",
      "Header.activeBackground":"hover",
      "Header.foreground":      "text",
      "Header.inactiveForeground": "textMuted",
      "Header.borderColor":     "border",
      "HeaderCloseButton.background": "chrome",
      "Button.selectedBackground": "selection",
      "Button.selectedForeground": "text"
    },

    "Tree": {
      "background":             "sidebar",
      "foreground":             "text",
      "selectionBackground":    "selection",
      "selectionForeground":    "text",
      "selectionInactiveBackground": "selectionInactive",
      "hoverBackground":        "hover",
      "modifiedItemForeground": "warning",
      "errorForeground":        "error",
      "rowHeight":              "22"
    },

    "VersionControl.FileHistory.Commit": {
      "selectedBackground":     "selection",
      "selectedForeground":     "text"
    },

    "WelcomeScreen": {
      "background":             "background",
      "foreground":             "text",
      "captionForeground":      "text",
      "separatorColor":         "border",
      "Projects.background":    "chrome",
      "Projects.selectionBackground": "selection",
      "Projects.selectionInactiveBackground": "selectionInactive",
      "Projects.foreground":    "text",
      "Details.background":     "background",
      "GroupIcon.borderColor":  "border",
      "headerBackground":       "chrome"
    }
  }
}
```

- [ ] **Step 2: Verify the file was created**

```bash
ls jetbrains-plugin/src/main/resources/themes/
```

Expected output: `Electronic Moonlight.theme.json`

---

### Task 2: Update plugin.xml to register the theme provider

**Files:**
- Modify: `jetbrains-plugin/src/main/resources/META-INF/plugin.xml`

- [ ] **Step 1: Replace the extensions block**

Open `jetbrains-plugin/src/main/resources/META-INF/plugin.xml` and replace the entire `<extensions>` block:

**Before:**
```xml
  <extensions defaultExtensionNs="com.intellij">
    <bundledColorScheme path="/colors/Electronic Moonlight"/>
  </extensions>
```

**After:**
```xml
  <extensions defaultExtensionNs="com.intellij">
    <themeProvider id="com.electronicmoonlight.theme"
                   path="/themes/Electronic Moonlight.theme.json"/>
  </extensions>
```

The full file should now be:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<idea-plugin>
  <id>com.electronicmoonlight.theme</id>
  <name>Electronic Moonlight Theme</name>
  <version>1.0.0</version>
  <vendor>Electronic Moonlight</vendor>
  <description>Electronic Moonlight color scheme for JetBrains IDEs (Rider, IntelliJ, etc.).</description>
  <depends>com.intellij.modules.platform</depends>
  <idea-version since-build="221.0" />

  <extensions defaultExtensionNs="com.intellij">
    <themeProvider id="com.electronicmoonlight.theme"
                   path="/themes/Electronic Moonlight.theme.json"/>
  </extensions>
</idea-plugin>
```

- [ ] **Step 2: Commit**

```bash
git add jetbrains-plugin/src/main/resources/themes/ \
        jetbrains-plugin/src/main/resources/META-INF/plugin.xml
git commit -m "feat: add full JetBrains UI theme (themeProvider + theme.json)"
```

---

### Task 3: Build and verify

**Files:** No source changes — verify build output only.

- [ ] **Step 1: Build the plugin**

```bash
cd jetbrains-plugin && ./gradlew assemble
```

Expected output ends with:
```
BUILD SUCCESSFUL
```

- [ ] **Step 2: Verify the zip contains the theme file**

```bash
unzip -l build/distributions/electronic-moonlight-jetbrains-plugin-1.0.0.zip
```

Expected: you should see `ElectronicMoonlight/lib/electronic-moonlight-plugin-1.0.0.jar` (the themes directory is bundled inside the jar, not listed separately).

- [ ] **Step 3: Verify the theme file is inside the jar**

```bash
jar tf build/libs/electronic-moonlight-plugin-1.0.0.jar
```

Expected output includes:
```
META-INF/plugin.xml
colors/Electronic Moonlight.icls
themes/Electronic Moonlight.theme.json
```

- [ ] **Step 4: Install in Rider and verify**

1. In Rider: **Settings → Plugins → ⚙ → Install Plugin from Disk**
2. Select `jetbrains-plugin/build/distributions/electronic-moonlight-jetbrains-plugin-1.0.0.zip`
3. Restart Rider
4. Open **Settings → Appearance & Behavior → Appearance → Theme**
5. Confirm **Electronic Moonlight** appears in the dropdown
6. Select it and confirm the IDE chrome (sidebar, tabs, toolbar, status bar) changes to the dark blue/purple palette

- [ ] **Step 5: Commit build confirmation note**

No code changes needed — build artifacts are gitignored. The feature is complete when the theme appears in Rider's Appearance → Theme dropdown.
