# Publishing to JetBrains Marketplace

This document explains the minimal steps to publish the `Electronic Moonlight` color-scheme plugin to the JetBrains Marketplace.

## Prerequisites
- JetBrains account (plugins.jetbrains.com).
- A plugin ZIP (we already created `electronic-moonlight-jetbrains-plugin.zip` in the repo root).
- A short description, version number, and an optional icon (recommended: 40×40 PNG).

## Quick manual publish (fastest)
1. Sign in at https://plugins.jetbrains.com with your JetBrains account.
2. Click **Create New Plugin** and fill in name, ID (use `com.electronicmoonlight.theme`), and vendor.
3. Upload the ZIP created earlier (`electronic-moonlight-jetbrains-plugin.zip`).
4. Add screenshots, icon, and release notes.
5. Submit / Publish. The plugin listing will appear after review.

## Prepare your plugin properly
- Ensure `META-INF/plugin.xml` contains correct `<id>`, `<name>`, `<version>` and `<description>`.
- Set compatibility via `<idea-version since-build="..." until-build="..."/>` if needed.
- Add an icon to `resources/icons` and reference it in Marketplace metadata.

## Testing before publish
- Install from disk in any JetBrains IDE: Preferences → Plugins → Install Plugin from Disk… → select the ZIP.
- Verify scheme appears: Preferences → Editor → Color Scheme → `Electronic Moonlight`.

## Automating publish with Gradle (recommended for future releases)
1. Add the Gradle IntelliJ Plugin to your plugin build (example Kotlin DSL snippet):

```kotlin
plugins {
  id("org.jetbrains.intellij") version "1.13.3"
}

intellij {
  version.set("2022.3")
  type.set("IC")
  pluginName.set("Electronic Moonlight Theme")
}

tasks.publishPlugin {
  token.set(System.getenv("JB_PUBLISH_TOKEN"))
}
```

2. Create a publishing token on the JetBrains website (Account → Settings → Create Token).
3. Locally set the token and publish:

```bash
export JB_PUBLISH_TOKEN="<your-token>"
./gradlew publishPlugin
```

Notes:
- The Gradle approach uploads the plugin directly to JetBrains and can create releases automatically.
- Marketplace may review before public availability.

## Post-publish checklist
- Add release notes and changelog entries.
- Update `version` in `META-INF/plugin.xml` for subsequent releases.
- Consider adding CI to build the ZIP and call `publishPlugin` with the token stored as a secret.

----

If you want, I can:
- (A) Add a `build.gradle.kts` example inside `jetbrains-plugin` to enable `./gradlew publishPlugin`.
- (B) Commit and tag the current plugin snapshot and create a draft release.
- (C) Draft the Marketplace listing text and image suggestions.
