[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (str) Application entry point
# Name of the file that contains the entry point to your app (main.py in your case)
entrypoint = main.py

# (list) Application requirements
# Specify the modules used in your app here
requirements = sdl2,python3,kivy==2.3.0,kivy_garden,geopy,pyperclip,requests,overpass

# (list) Garden requirements
# Specify any Kivy Garden packages used in your app here
garden_requirements = kivy_garden.mapview

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
# Permissions that your app needs (INTERNET is necessary for network operations)
android.permissions = INTERNET

# (bool) Enable android storage permission
android.permission.storage = True

# (str) The package format for android
android.arch = armeabi-v7a

# (str) Path to the icon file
icon.filename = %(source.dir)s/data/icon.png

# (str) Path to the presplash file
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Full name including namespace of the main activity
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including namespace of the Java class to launch the activity
#android.bootstrap = org.kivy.android.PythonBootstrap

# (list) Add screensavers support to your app
# (add screensavers from the screensavers repo to your project and include their names here)
#screensavers =


# (str) The service to run
#android.service = myservice:MyService

# (str) API keys
#api = 

# (str) The format used to package the app for Android
# Default is "release" but can be set to "debug" for testing.
android.package_type = debug

# (list) Android additional libraries
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_x86 = libs/android-x86/*.so

# (str) Path to a custom android NDK (if needed)
#android.ndk_path =

# (list) Android's SDK API to install (default is 27)
android.sdk = 28

# (str) Android's NDK version to use (default is 17c)
android.ndk = 25

# (str) Android's NDK API level to use (default is 21)
android.ndk_api = 21

# (list) Android additional Java dependencies
#android.add_jars =

# (list) Android additional libraries
#android.add_libs_armeabi_v7a =

# (list) Android additional libraries
#android.add_libs_x86 =

# (list) Android additional libraries
#android.add_libs_x86_64 =

# (list) Android additional libraries
#android.add_libs_arm64_v8a =

# (str) Keystore file
#android.release_keystore =

# (str) Keystore password
#android.release_keyalias =

# (str) Keystore alias password
#android.release_keypassword =

# (str) Custom source folders (if any)
# Add custom source folders to this list (comma separated)
#custom.source_folders = src

# (str) Custom build folder (if any)
#custom.build = 

# (str) Custom packaging options (if any)
#custom.packaging =

# (str) Name of the executable generated for your application (for android this is a .apk)
#executable =

# (list) Gradle dependencies
# A list of Gradle dependencies to use.
#gradle.dependencies = "com.android.support:appcompat-v7:27.1.1"

# (list) Additional python dependencies
#requirements.python =

# (str) Custom python build
#python.build =

# (str) Custom python build 
#python.root =

# (str) Path to the kivy source code to use (this can be a local directory, or a git url)
#kivy.source = 

# (str) Kivy git tag or branch to use (default is master)
#kivy.branch = master

# (str) Path to the buildozer plugins (if any)
#plugins.path =

# (list) Extra arguments to pass to the buildozer command
#buildozer.extra_args = 

# (str) Where to store build and distribution files (default is build/)
#builddir = build

# (str) Clean build directory before building
#clean_build_dir = True

# (str) App name as displayed in notifications
#notif.name = %(app_title)s

# (str) Use the Cython prebuilt binaries (this can make the build faster, only available for python 2.x)
#cython_binary =

# (list) Additional cython arguments
#cython_args =

# (str) The android log level (default is INFO)
#android.log_level = INFO

# (list) Screen sizes to exclude from apk
#screen.exclude =

# (list) Supported architectures
#arch = armeabi-v7a

# (str) The console log level (default is DEBUG)
#console.log_level = DEBUG

# (str) Log format
#console.log_format =

# (list) The build commands to execute (default is clean, update, build)
#build_commands = clean, update, build

# (str) The default build mode (default is release)
#build_mode = release

# (str) Path to the Android NDK (default is ~/.buildozer/android/platform/android-ndk-r20b)
#android.ndk_path =

# (str) Path to the Android SDK (default is ~/.buildozer/android/platform/android-sdk)
#android.sdk_path =

# (str) Path to a custom Android SDK
#android.custom_sdk_path =

# (str) Use a specific build platform (default is auto)
#android.build_platform = auto

# (str) Path to your kivy app (default is .)
#app.root = .

# (str) The package format for iOS
#ios.archs = arm64, armv7, i386

# (str) The Xcode project folder
#ios.xcode = 

# (str) Full path to your iOS certificate
#ios.certificate =

# (str) Full path to your iOS provisioning profile
#ios.profile =

# (str) Full path to your iOS team ID
#ios.team =

# (str) The version of the OpenSSL library to use
#openssl =

# (str) The version of the sqlite3 library to use
#sqlite =

# (str) The version of the SDL2 library to use
#sdl2 =

# (str) The version of the Pygame library to use
#pygame =

# (str) Path to your iOS app icon (default is .)
#ios.icon_path = 

# (str) Path to your iOS launch image (default is .)
#ios.launch_image_path = 

# (str) Full path to the directory containing your iOS framework files (if any)
#ios.frameworks_path = 

# (str) Full path to the directory containing your iOS resource files (if any)
#ios.resources_path = 

# (str) Full path to the directory containing your iOS asset catalog files (if any)
#ios.assets_path = 

# (str) The minimum iOS version to support (default is 9.0)
#ios.min_version = 9.0

# (list) List of Xcode targets to build (default is all)
#xcode.targets = all

# (str) Custom Xcode schemes
#xcode.schemes = 

# (list) Additional iOS build settings
#ios.build_settings =

# (list) List of files to be included in the Xcode project
#xcode.extra_files =

# (list) List of files to be included in the Android project
#android.extra_files =

# (list) List of files to be included in the iOS project
#ios.extra_files =

# (str) Path to your custom python script (if any)
#python.custom_script =

# (str) The path to a custom main.c file (for advanced use only)
#android.custom_main =

# (str) Custom cython build command
#cython.build =

# (str) Custom build commands (default is update, clean, build)
#build_commands = update, clean, build

# (str) Build the app in a specific architecture (default is armeabi-v7a)
#android.arch = armeabi-v7a

# (str) Custom name for the apk file (default is %(package.name)s)
#android.apk_name =

# (str) Custom name for the iOS app (default is %(app_title)s)
#ios.app_name =

# (list) Custom args to pass to the android build system
#android.extra_args =

# (list) Custom args to pass to the ios build system
#ios.extra_args =

# (str) Path to the Java development kit
#java.jdk =

# (list) Additional android.manifest permissions
#android.add_permissions =

# (str) The platform used to build the app
#platform = 

# (list) List of files to include in the android project
#android.extra_files =

# (list) List of files to include in the ios project
#ios.extra_files =

# (list) List of build options
#build_options =

# (str) Custom cython path
#cython.path =

# (list) Custom android manifest permissions
#android.add_permissions =

# (str) Custom android ant options
#android.ant_options =

# (str) Path to a custom keystore file
#android.release_keystore =

# (str) Custom keystore password
#android.release_keypassword =

# (str) Custom keystore alias password
#android.release_keyalias =

# (str) Full path to your custom Java class
#android.custom_class =

# (str) Path to the custom manifest file
#android.manifest =

# (str) Custom android plugin
#android.plugin =

# (str) Additional arguments to pass to the android build system
#android.extra_args =

# (str) Additional arguments to pass to the ios build system
#ios.extra_args =

# (str) Additional arguments to pass to the cython build system
#cython.extra_args =

# (str) Full path to the Kivy source code
#kivy.source = 

# (str) Kivy git branch to use (default is master)
#kivy.branch = master

# (list) Additional python dependencies
#python.dependencies =

# (str) Full path to your custom Kivy framework file
#kivy.framework =

# (str) Full path to your custom Kivy resource file
#kivy.resources =

# (str) Full path to your custom Kivy asset file
#kivy.assets =

# (list) Additional Kivy settings
#kivy.settings =

# (str) Full path to the custom android bootstrap file
#android.bootstrap =

# (list) Additional android libraries
#android.additional_libs =

# (str) The minimum API level to support
#android.minapi = 21

# (str) Full path to the android SDK
#android.sdk_path =

# (str) Path to the Android NDK
#android.ndk_path =

# (list) List of android extra directories
#android.extra_dirs =

# (str) List of additional android manifest permissions
#android.add_permissions =

# (list) List of android build options
#android.build_options =

# (str) Path to the custom android bootstrap file
#android.bootstrap =

# (str) Path to the custom android NDK
#android.ndk_path =

# (str) Custom android NDK build command
#android.ndk_build =

# (list) List of additional python requirements
#python.requirements =

# (str) Full path to your custom python script
#python.custom_script =

# (str) Full path to your custom python library
#python.library =

# (str) Custom python command
#python.command =

# (str) The default python executable to use
#python.executable =

# (list) List of python extra directories
#python.extra_dirs =

# (str) List of additional python dependencies
#python.dependencies =

# (str) Path to the custom python script file
#python.script =

# (str) Custom python build command
#python.build =

# (str) The python version to use (default is 3)
#python.version = 3

# (str) Path to the custom python setup file
#python.setup =

# (list) Additional Kivy settings
#kivy.settings =

# (str) Custom Kivy build command
#kivy.build =

# (str) Full path to the Kivy source code
#kivy.source =

# (list) List of Kivy extra directories
#kivy.extra_dirs =

# (str) List of additional Kivy dependencies
#kivy.dependencies =

# (str) Full path to your custom Kivy framework file
#kivy.framework =

# (str) Full path to your custom Kivy resource file
#kivy.resources =

# (str) Custom Kivy command
#kivy.command =

# (list) List of Kivy build options
#kivy.build_options =

# (str) The Kivy version to use (default is 1.11.1)
#kivy.version =

# (list) List of android additional manifest permissions
#android.add_permissions =

# (list) List of additional android directories
#android.extra_dirs =

# (str) The minimum SDK version to support (default is 21)
#android.minsdk = 21

# (str) Path to the custom android build file
#android.build =

# (str) Path to the custom android NDK
#android.ndk =

# (list) List of android build options
#android.build_options =

# (str) Path to the custom android bootstrap file
#android.bootstrap =

# (str) Path to the custom android NDK
#android.ndk =

# (str) Path to the custom android SDK
#android.sdk =

# (str) The package format for android
#android.arch =

# (str) Path to the custom android build file
#android.build =

# (str) Custom android command
#android.command =

# (list) List of additional android directories
#android.extra_dirs =

# (list) List of additional android build options
#android.build_options =

# (str) Path to the custom android bootstrap file
#android.bootstrap =

# (str) Path to the custom android SDK
#android.sdk =

# (str) Path to the custom android NDK
#android.ndk =

# (str) Path to the custom android build file
#android.build =

# (str) Custom android build command
#android.build_command =

# (str) Custom android command
#android.command =

# (list) List of additional android build options
#android.build_options =

# (list) List of additional android manifest permissions
#android.add_permissions =

# (list) List of android additional directories
#android.extra_dirs =

# (list) List of additional android libraries
#android.additional_libs =

# (list) List of android extra directories
#android.extra_dirs =

# (list) List of android build options
#android.build_options =

# (list) List of additional android libraries
#android.additional_libs =

# (str) Path to the custom android build file
#android.build =

# (str) Custom android command
#android.command =

# (str) Path to the custom android SDK
#android.sdk =

# (str) Path to the custom android NDK
#android.ndk =

# (str) Custom android build command
#android.build_command =

# (str) Path to the custom android bootstrap file
#android.bootstrap =

# (str) The package format for android
#android.arch =

# (list) Additional Kivy requirements
#kivy.additional_requirements =

# (list) List of additional Kivy directories
#kivy.extra_dirs =

# (str) Custom Kivy build command
#kivy.build_command =

# (str) Path to the Kivy source code
#kivy.source =

# (list) List of Kivy build options
#kivy.build_options =

# (list) List of additional Kivy libraries
#kivy.additional_libs =

# (str) Path to the custom python setup file
#python.setup =

# (list) List of additional python directories
#python.extra_dirs =

# (str) Path to the custom python script file
#python.script =

# (str) Path to the custom python build file
#python.build =

# (str) Custom python build command
#python.build_command =

# (str) Custom python command
#python.command =

# (list) List of additional python requirements
#python.requirements =

# (list) List of additional python dependencies
#python.dependencies =
