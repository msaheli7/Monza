[app]

# (str) Title of your application
title = Monza

# (str) Package name
package.name = monza

# (str) Package domain (needed for android/ios packaging)
package.domain = org.monza

# (str) Source code where the main.py live
source.dir = .

# (str) The main .py file to use as the main entry point for you app
source.main = main.py

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (one of: landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions (example: INTERNET, WRITE_EXTERNAL_STORAGE)
android.permissions = INTERNET

# (int) Target API (most recent stable is recommended)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (int) Android NDK version to use
android.ndk = 25b

# (str) Application versioning (method 1)
version = 1.0

# (str) Application version code (used in Android)
version.code = 1

# (str) Application version name (used in Android)
version.name = "1.0"

# (str) Presplash of the application
presplash.filename =

# (str) Icon of the application
icon.filename =

[buildozer]

# (str) log level (info, debug, error)
log_level = 2

# (str) build output directory
build_dir = bin

# (bool) clean build (enforces a full rebuild)
clean = False

#warnings to be ignored
ignore_path = .git,.idea,__pycache__

