rootProject.name = "electronic-moonlight-theme"

pluginManagement {
	repositories {
		gradlePluginPortal()
		mavenCentral()
		maven {
			// JetBrains artifacts (structure-* and IntelliJ dependencies)
			url = uri("https://cache-redirector.jetbrains.com/intellij-dependencies")
		}
		maven {
			url = uri("https://cache-redirector.jetbrains.com/intellij-repository/releases")
		}
		maven {
			// JetBrains plugin repository (contains structure-* artifacts)
			url = uri("https://plugins.jetbrains.com/maven")
		}
		maven {
			// Additional JetBrains packages repo
			url = uri("https://packages.jetbrains.team/maven/p/intellij/plugins")
		}
	}
}
