# <img src="https://github.com/EfazDev/roblox-bootstrap/blob/main/BootstrapImages/AppIcon.png?raw=true" width="40" height="40" align="left">Efaz's Roblox Bootstrap
## Customize your Roblox limitations to a new level!

![Multiple Roblox Instances with Pet Sim Opened](https://github.com/EfazDev/roblox-bootstrap/blob/main/BootstrapImages/MultipleInstances.png?raw=true)
![Subway Surfers Avatar Map](https://github.com/EfazDev/roblox-bootstrap/blob/main/BootstrapImages/AvatarEditor.png?raw=true)
![Server Location Notification](https://github.com/EfazDev/roblox-bootstrap/blob/main/BootstrapImages/ServerLocations.png?raw=true)
![Discord Rich Presences](https://github.com/EfazDev/roblox-bootstrap/blob/main/BootstrapImages/DiscordPresences.png?raw=true)

## What is this?
Efaz's Roblox Bootstrap is a program inspired by Bloxstrap but using only Python and also on macOS! It also uses [Activity Tracking](https://github.com/pizzaboxer/bloxstrap/wiki/What-is-activity-tracking%3F) and [BloxstrapRPC](https://github.com/pizzaboxer/bloxstrap/wiki/Integrating-Bloxstrap-functionality-into-your-game)!

## Features
1. Set FFlag Customizations on your Roblox installation!
2. Set a custom Avatar Map, App Icon, Cursor, Mod Mode, and Death Sound!
3. Use multiple instances directly by launching from your default web browser or the EfazRobloxBootstrap app! [macOS only]
4. Get server locations when joining (also uses ipinfo.io like Bloxstrap)
5. Discord Rich Presences [Includes Support for BloxstrapRPC]

## Requirements
1. [Full ZIP file](https://github.com/EfazDev/roblox-bootstrap/archive/refs/heads/main.zip)
2. [Python 3.12](https://www.python.org/downloads/) (You may install from InstallPython.sh)
3. Python Modules: pip install pypresence requests (For Windows: pip install pypresence requests pywin32 plyer)

## Install
1. Once you got all the requirements, run Install.py and once it says Success, you may use the Bootstrap now!
2. [In order to configure settings, register URL Schemes or more, open the app by going to the Applications folder and open EfazRobloxBootstrapLoader.app]

## Credits
1. Main Coding by <span style="color:#FF8700">@EfazDev</span>
2. Old Death Sound and Cursors were sourced from <span style="color:#FF5FFF">[Bloxstrap files](https://github.com/pizzaboxer/bloxstrap)</span>
3. AvatarEditorMaps were from <span style="color:#FF00FF">[Mielesgames's Map Files](https://github.com/Mielesgames/RobloxAvatarEditorMaps)</span> slightly edited to be usable for the current version of Roblox (as of the time of writing this)
4. Some files were exported from the main macOS Roblox.app or Bloxstrap files. <span style="color:#FF8700">(Logo was made by the Apple Pages app icon, recolored and then added the Roblox Logo)</span>
5. macOS App was built using <span style="color:#00AFFF">pyinstaller</span>. You can recreate and deploy using this command: <span style="color:#00AFFF">pyinstaller EfazRobloxBootstrap.spec --distpath Apps --noconfirm && rm -rf build ./Apps/EfazRobloxBootstrapLoad/ && python3 Install.py --install</span> <span style="color:#FFFF00">[WARNING]: This command can only be used using native macOS so a virtual machine may be needed and can reduce security.</span>
6. Windows App was also built using <span style="color:#00AFFF">pyinstaller</span>. You can recreate and deploy using this command: <span style="color:#00AFFF">pyinstaller EfazRobloxBootstrap_Windows.spec --distpath Apps --noconfirm && python Install.py --install</span> <span style="color:#FFFF00">[WARNING]: This command also can only be used using Windows and can reduce security.</span>