Theme install notes — Electronic Moonlight

JetBrains Rider (macOS)
- Copy `jetbrains/Electronic Moonlight.icls` to:
  `~/Library/Preferences/<PRODUCT>/colors/` or
  `~/Library/Application Support/JetBrains/<IDE>/colors/` (product/version varies).
- Or in Rider open `Preferences → Editor → Color Scheme` → cog icon → `Import Scheme...` and select the `.icls` file.

Xcode (macOS)
- Create the folder if missing: `~/Library/Developer/Xcode/UserData/FontAndColorThemes/`
- Copy `xcode/Electronic Moonlight.xccolortheme` into that folder and restart Xcode.

Notes
- This is a best-effort mapping of the most commonly used editor/token colors from your VS Code theme. Some platform-specific tokens may not map exactly; tell me which areas you want tuned (UI, sidebar, terminals, specific languages) and I will refine.

Terminal & iTerm2
- I added `iterm/Electronic Moonlight.itermcolors` which maps the VS Code ANSI/terminal colors. To import in iTerm2: `iTerm2 → Preferences → Profiles → Colors → Color Presets... → Import...` and choose the `.itermcolors` file.
- The iTerm file preserves alpha for selection where supported. Terminal emulators vary in alpha support; iTerm preserves it while JetBrains console uses opaque hex values.

JetBrains Rider refinements
- I expanded `jetbrains/Electronic Moonlight.icls` to include more UI-like mappings (status bar, sidebar, tabs) and full console ANSI colors. JetBrains color schemes are primarily for editor and console coloring; some VS Code UI chrome cannot be represented exactly.

If you want I can:
- Further tune Rider UI elements (tool windows, gutter, diff colors).
- Add language-specific JetBrains attributes (e.g., Swift/C#) to improve syntax parity.
- Produce an iTerm2 + macOS Terminal profile if you use Terminal.app.

