[app]

# (str) Title of your application
title = DeLocator

# (str) Package name
package.name = DeLocator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.delocator

# (str) Source code where the main.py live
source.dir = .

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = kivy, kivy_garden.mapview, geopy, requests, overpass, pyperclip

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, ACCESS_FINE_LOCATION

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
