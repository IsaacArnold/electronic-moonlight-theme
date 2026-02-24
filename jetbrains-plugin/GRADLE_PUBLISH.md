# Publishing with Gradle

The `build.gradle.kts` and `./gradlew` wrapper in this folder enable you to build and publish directly to JetBrains Marketplace using Gradle.

## Quick Start: Publish to Marketplace

1. **Get a JetBrains API token:**
   - Sign in to https://plugins.jetbrains.com  
   - Account → Settings → Create Token  
   - Copy the token

2. **Publish:**
   ```bash
   cd jetbrains-plugin
   export JB_PUBLISH_TOKEN="<your-token>"
   ./gradlew publishPlugin
   ```

   On Windows:
   ```cmd
   cd jetbrains-plugin
   set JB_PUBLISH_TOKEN=<your-token>
   gradlew publishPlugin
   ```

## Other Useful Commands

**Build the plugin ZIP (without publishing):**
```bash
./gradlew buildPlugin
```
Output: `build/distributions/electronic-moonlight-theme-1.0.0.zip`

**View all available tasks:**
```bash
./gradlew tasks
```

## For Future Releases

1. Update the version in `build.gradle.kts` (e.g., `version = "1.1.0"`)
2. Update `META-INF/plugin.xml` with new version if needed
3. Run `./gradlew publishPlugin` to release

## Security Notes
- Never commit your `JB_PUBLISH_TOKEN` to version control.
- Store the token as a CI/CD secret if automating releases (GitHub Actions, GitLab CI, etc.).

## Troubleshooting

If you encounter Gradle compatibility issues:
- Ensure you have Java 11+ installed: `java -version`
- Clear cache and retry: `rm -rf .gradle && ./gradlew publishPlugin`
- Use the system Gradle instead: `gradle publishPlugin` (requires Gradle 8.5+ installed)

