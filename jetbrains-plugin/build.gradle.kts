plugins {
  id("java")
  id("base")
}

group = "com.electronicmoonlight"
version = "1.0.0"

// Use a fixed Java toolchain so the build works even when the system JDK
// is newer than what Kotlin/Gradle understand (e.g. JDK 25). JetBrains
// plugin builds are happy on Java 17, which is still widely available.
java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(17))
    }
}

repositories {
  mavenCentral()
}
// Add JetBrains repositories for IntelliJ dependencies
repositories {
  mavenCentral()
  maven {
    url = uri("https://cache-redirector.jetbrains.com/intellij-dependencies")
  }
  maven {
    url = uri("https://cache-redirector.jetbrains.com/intellij-repository/releases")
  }
  maven {
    url = uri("https://plugins.jetbrains.com/maven")
  }
  maven {
    url = uri("https://packages.jetbrains.team/maven/p/intellij/plugins")
  }
}

// Build a standard jar that includes `src/main/resources` (so META-INF/plugin.xml
// will be inside the jar). Then assemble a plugin zip that places the jar into a
// top-level `lib/` directory (this matches JetBrains plugin ZIP layout requirements).

tasks.named<Jar>("jar") {
  archiveBaseName.set("electronic-moonlight-plugin")
  from(sourceSets.main.get().output)
}

tasks.register<Zip>("assemblePluginZip") {
  dependsOn(tasks.named("jar"))
  archiveBaseName.set("electronic-moonlight-jetbrains-plugin")
  destinationDirectory.set(layout.buildDirectory.dir("distributions"))
  into("lib") {
    from(tasks.named("jar"))
  }
}

// Make `assemble` produce the plugin zip as well
tasks.named("assemble") {
  dependsOn(tasks.named("assemblePluginZip"))
}
