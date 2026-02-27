# Electronic Moonlight — JetBrains plugin

This folder is a minimal JetBrains plugin packaging the `Electronic Moonlight` color scheme.

Build the plugin archive with Gradle (the old placeholder zip has been
removed to avoid confusion):

```sh
cd jetbrains-plugin
./gradlew assemble    # ZIP lands in build/distributions
```

1. Preferences → Plugins → **Install Plugin from Disk...**
2. Select `jetbrains-plugin/build/distributions/electronic-moonlight-jetbrains-plugin.zip`
3. Restart the IDE.

After restart: Preferences → Editor → Color Scheme → choose `Electronic Moonlight`.

Or install the scheme manually by copying `resources/colors/Electronic Moonlight.icls` into the IDE config `colors/` folder.

Or install the scheme manually by copying `resources/colors/Electronic Moonlight.icls` into the IDE config `colors/` folder.
