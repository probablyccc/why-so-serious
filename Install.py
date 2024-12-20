import shutil
import os
import platform
import json
import subprocess
import time
import sys
import RobloxFastFlagsInstaller
from PipHandler import pip

def printMainMessage(mes): print(f"\033[38;5;255m{mes}\033[0m")
def printErrorMessage(mes): print(f"\033[38;5;196m{mes}\033[0m")
def printSuccessMessage(mes): print(f"\033[38;5;82m{mes}\033[0m")
def printWarnMessage(mes): print(f"\033[38;5;202m{mes}\033[0m")
def printYellowMessage(mes): print(f"\033[38;5;226m{mes}\033[0m")
def printDebugMessage(mes): print(f"\033[38;5;226m{mes}\033[0m")

def isYes(text): return text.lower() == "y" or text.lower() == "yes"
def isNo(text): return text.lower() == "n" or text.lower() == "no"
def isRequestClose(text): return text.lower() == "exit" or text.lower() == "exit()"
def is_x86_windows():
    if platform.system() == "Windows":
        if platform.architecture()[0] == "32bit":
            return True
    return False
def copy_with_symlinks(src, dest, ignore_files=[]):
    for i in ignore_files:
        if i in src:
            return
    if os.path.lexists(dest):
        if os.path.isdir(dest) and not os.path.islink(dest):
            pass
        else:
            os.remove(dest)
    if os.path.islink(src):
        os.symlink(os.readlink(src), dest)
    elif os.path.isdir(src):
        os.makedirs(dest, exist_ok=True)
        for item in os.listdir(src):
            if item in ignore_files:
                continue
            copy_with_symlinks(os.path.join(src, item), os.path.join(dest, item))
    else:
        shutil.copy2(src, dest)

if __name__ == "__main__":
    main_os = platform.system()
    stored_main_app = {
        "Darwin": ["/Applications/EfazRobloxBootstrap.app", "/Applications/EfazRobloxBootstrapLoader.app", "/Applications/Play Roblox.app"],
        "Windows": [os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap"), os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap", "EfazRobloxBootstrap.exe"), os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap")]
    }
    ignore_files = ["build", "__pycache__", "LICENSE", "README.md", "InstallPython.sh", "FastFlagConfiguration.json", ".git"]
    current_version = {"version": "1.2.3"}
    instant_install = False
    silent_mode = False
    disable_remove_other_operating_systems = False
    pip_class = pip()

    handler = RobloxFastFlagsInstaller.Main()
    def ignore_files_func(dir, files): return set(ignore_files) & set(files)

    if "--install" in sys.argv:
        instant_install = True

    if "--silent" in sys.argv:
        silent_mode = True
        def printMainMessage(mes): silent_mode = True
        def printErrorMessage(mes): print(f"\033[38;5;196m{mes}\033[0m")
        def printSuccessMessage(mes): silent_mode = True
        def printWarnMessage(mes): silent_mode = True
        def printDebugMessage(mes): silent_mode = True
    else:
        os.system("cls" if os.name == "nt" else "clear")

    if "--disable-remove" in sys.argv:
        disable_remove_other_operating_systems = True

    printWarnMessage("-----------")
    printWarnMessage("Welcome to Efaz's Roblox Bootstrap Installer!")
    printWarnMessage("Made by Efaz from efaz.dev!")
    printWarnMessage(f"v{current_version['version']}")
    printWarnMessage("-----------")
    # Requirement Checks
    if main_os == "Windows":
        printMainMessage(f"System OS: {main_os}")
        found_platform = "Windows"
    elif main_os == "Darwin":
        printMainMessage(f"System OS: {main_os} (macOS)")
        found_platform = "Darwin"
    else:
        printErrorMessage("Efaz's Roblox Bootstrap is only supported for macOS or Windows.")
        input("> ")
        sys.exit(0)
    current_python_version = platform.python_version_tuple()
    if current_python_version < ("3", "10", "0"):
        printErrorMessage("Please update your current installation of Python above 3.10.0")
        input("> ")
        sys.exit(0)
    else:
        printMainMessage(f"Python Version: {platform.python_version()}")
    if main_os == "Windows":
        installation_folder = f"{handler.getRobloxInstallFolder()}\\"
        if not os.path.exists(installation_folder):
            printErrorMessage("Please install Roblox from the Roblox website in order to use this bootstrap!")
            input("> ")
            sys.exit(0)
        else:
            cur_vers = handler.getCurrentClientVersion()
            if cur_vers["success"] == True:
                printMainMessage(f"Current Roblox Version: {cur_vers['version']}")
            else:
                printErrorMessage("Something went wrong trying to determine your current Roblox version.")
                input("> ")
                sys.exit(0)
    elif main_os == "Darwin":
        if os.path.exists("/Applications/Roblox.app/"):
            cur_vers = handler.getCurrentClientVersion()
            if cur_vers["success"] == True:
                printMainMessage(f"Current Roblox Version: {cur_vers['version']}")
            else:
                printErrorMessage("Something went wrong trying to determine your current Roblox version.")
                input("> ")
                sys.exit(0)
        else:
            printErrorMessage("Please install Roblox from the Roblox website in order to use this bootstrap!")
            input("> ")
            sys.exit(0)
    overwrited = False
    if os.path.exists(stored_main_app[found_platform][0]) and os.path.exists(stored_main_app[found_platform][1]):
        overwrited = True
    def install():
        try:
            import requests
            import plyer
            import pypresence
            if main_os == "Darwin":
                import posix_ipc
                import objc
            elif main_os == "Windows":
                import win32com.client
        except Exception as e:
            printMainMessage("Some modules are not installed and may be needed for some features. Do you want to install all the modules needed now? (y/n)")
            if instant_install == True or isYes(input("> ")) == True:
                pip_class.install(["requests", "plyer", "pypresence"])
                if main_os == "Darwin":
                    pip_class.install(["posix-ipc", "pyobjc"])
                elif main_os == "Windows":
                    pip_class.install(["pywin32"])
                printSuccessMessage("Successfully installed modules!")
            else:
                printErrorMessage("Ending installation..")
                sys.exit(0)
        if os.path.exists("./Apps/"):
            if main_os == "Darwin":
                if os.path.exists(f"./Apps/EfazRobloxBootstrapMac.zip"):
                    # Unzip Installation ZIP
                    printMainMessage("Unzipping Installation ZIP File..")
                    try:
                        subprocess.run(["unzip", "-o", f"./Apps/EfazRobloxBootstrapMac.zip", "-d", f"./Apps/EfazRobloxBootstrapMac"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                    except Exception as e:
                        printErrorMessage(f"Something went wrong while trying to unzip macOS apps file: {str(e)}")
                    time.sleep(1)
                else:
                    printYellowMessage("Something went wrong finding EfazRobloxBootstrapMac.zip. It will require a EfazRobloxBootstrapMac folder in order for installation to finish.")
                if os.path.exists(f"./Apps/EfazRobloxBootstrapMac/"):
                    # Get FastFlagConfiguration.json Data
                    if overwrited == True:
                        printMainMessage("Getting Configuration File Data..")
                        fast_config_path = os.path.join(stored_main_app[found_platform][0], "Contents", "Resources", "FastFlagConfiguration.json")
                        if os.path.exists(fast_config_path):
                            with open(fast_config_path, "r") as f:
                                fastFlagConfig = json.load(f)
                        else:
                            fastFlagConfig = {}
                    else:
                        fastFlagConfig = {}

                    # Delete Other Operating System Files
                    if not (disable_remove_other_operating_systems == True):
                        deleted_other_os = False
                        if os.path.exists("./Apps/EfazRobloxBootstrap/"):
                            shutil.rmtree("./Apps/EfazRobloxBootstrap/")
                            deleted_other_os = True
                        if os.path.exists("./Apps/EfazRobloxBootstrap32/"):
                            shutil.rmtree("./Apps/EfazRobloxBootstrap32/")
                            deleted_other_os = True
                        if deleted_other_os == True: printMainMessage("To help save space, the script has automatically deleted files made for other operating systems!")

                    # Insert New Display Names
                    printMainMessage("Adding Display Names..")
                    if os.path.exists("/Applications/EfazRobloxBootstrap.app/Contents/Info.plist"):
                        dis = handler.readPListFile("/Applications/EfazRobloxBootstrap.app/Contents/Info.plist")
                        dis["CFBundleDisplayName"] = "Efaz's Roblox Bootstrap"
                        dis["CFBundleShortVersionString"] = current_version["version"]
                        dis["CFBundleVersion"] = current_version["version"]
                        handler.writePListFile("/Applications/EfazRobloxBootstrap.app/Contents/Info.plist", dis)
                    if os.path.exists("/Applications/EfazRobloxBootstrapLoader.app/Contents/Info.plist"):
                        dis = handler.readPListFile("/Applications/EfazRobloxBootstrapLoader.app/Contents/Info.plist")
                        dis["CFBundleDisplayName"] = "Load Efaz's Roblox Bootstrap"
                        dis["CFBundleShortVersionString"] = current_version["version"]
                        dis["CFBundleVersion"] = current_version["version"]
                        handler.writePListFile("/Applications/EfazRobloxBootstrapLoader.app/Contents/Info.plist", dis)
                    if os.path.exists("/Applications/Play Roblox.app/Contents/Info.plist"):
                        dis = handler.readPListFile("/Applications/Play Roblox.app/Contents/Info.plist")
                        dis["CFBundleDisplayName"] = "Play Roblox"
                        dis["CFBundleShortVersionString"] = current_version["version"]
                        dis["CFBundleVersion"] = current_version["version"]
                        handler.writePListFile("/Applications/Play Roblox.app/Contents/Info.plist", dis)

                    # Delete frameworks if there's extra
                    if True:
                        printMainMessage("Clearing App Frameworks..")
                        if os.path.exists("/Applications/EfazRobloxBootstrap.app/Contents/Frameworks/"):
                            shutil.rmtree("/Applications/EfazRobloxBootstrap.app/Contents/Frameworks/")
                        if os.path.exists("/Applications/EfazRobloxBootstrapLoader.app/Contents/Frameworks/"):
                            shutil.rmtree("/Applications/EfazRobloxBootstrapLoader.app/Contents/Frameworks/")
                        if os.path.exists("/Applications/Play Roblox.app/Contents/Frameworks/"):
                            shutil.rmtree("/Applications/Play Roblox.app/Contents/Frameworks/")

                    # Convert All Mod Modes to Mods
                    if os.path.exists("./ModModes/"):
                        printMainMessage("Converting Mod Modes to Mods..")
                        for i in os.listdir("./ModModes/"):
                            mod_mode_path = os.path.join("./ModModes/", i)
                            if os.path.isdir(mod_mode_path):
                                if not os.path.exists(f"./Mods/{i}/"):
                                    os.makedirs(f"./Mods/{i}/", exist_ok=True)
                                shutil.copytree(mod_mode_path, f"./Mods/{i}/", dirs_exist_ok=True)
                        shutil.rmtree("./ModModes/")
                    if os.path.exists("/Applications/EfazRobloxBootstrap.app/Contents/Resources/ModModes/"):
                        printMainMessage("Converting Mod Modes to Mods..")
                        for i in os.listdir("/Applications/EfazRobloxBootstrap.app/Contents/Resources/ModModes/"):
                            mod_mode_path = os.path.join("/Applications/EfazRobloxBootstrap.app/Contents/Resources/ModModes/", i)
                            if os.path.isdir(mod_mode_path):
                                if not os.path.exists(f"/Applications/EfazRobloxBootstrap.app/Contents/Resources/Mods/{i}/"):
                                    os.makedirs(f"/Applications/EfazRobloxBootstrap.app/Contents/Resources/Mods/{i}/", exist_ok=True)
                                shutil.copytree(mod_mode_path, f"/Applications/EfazRobloxBootstrap.app/Contents/Resources/Mods/{i}/", dirs_exist_ok=True)
                        shutil.rmtree("/Applications/EfazRobloxBootstrap.app/Contents/Resources/ModModes/")
                    
                    # Install to /Applications/
                    printMainMessage("Installing to Applications Folder..")
                    if os.path.exists(stored_main_app[found_platform][0]):
                        copy_with_symlinks(f"./Apps/EfazRobloxBootstrapMac/Apps/EfazRobloxBootstrap.app", stored_main_app[found_platform][0], ignore_files=ignore_files)
                    else:
                        copy_with_symlinks(f"./Apps/EfazRobloxBootstrapMac/Apps/EfazRobloxBootstrap.app", stored_main_app[found_platform][0])
                    copy_with_symlinks(f"./Apps/EfazRobloxBootstrapMac/Apps/EfazRobloxBootstrapLoad.app", stored_main_app[found_platform][1])
                    copy_with_symlinks(f"./Apps/EfazRobloxBootstrapMac/Apps/PlayRoblox/Play Roblox.app", stored_main_app[found_platform][2])

                    # Prepare Contents of .app files
                    printMainMessage("Preparing Contents..")
                    if os.path.exists(stored_main_app[found_platform][0]):
                        # Add App Icon for Finder to cache
                        printMainMessage("Adding App Icon..")
                        shutil.copy(f"AppIcon.icns", f"{stored_main_app[found_platform][0]}/Icon")

                        # Export ./ to /Contents/Resources/
                        printMainMessage("Copying Main Resources..")
                        shutil.copytree(f"./", f"{stored_main_app[found_platform][0]}/Contents/Resources/", dirs_exist_ok=True, ignore=ignore_files_func, symlinks=True)
                        
                        # Remove Apps Folder in /Contents/Resources/
                        printMainMessage("Removing Apps Folder in /Contents/Resources/ to save space.")
                        if os.path.exists(os.path.join(stored_main_app[found_platform][0], "Contents", "Resources", "Apps")):
                            shutil.rmtree(os.path.join(stored_main_app[found_platform][0], "Contents", "Resources", "Apps"))
                        if os.path.exists(os.path.join(stored_main_app[found_platform][1], "Contents", "Resources", "Apps")):
                            shutil.rmtree(os.path.join(stored_main_app[found_platform][1], "Contents", "Resources", "Apps"))
                        if os.path.exists(os.path.join(stored_main_app[found_platform][2], "Contents", "Resources", "Apps")):
                            shutil.rmtree(os.path.join(stored_main_app[found_platform][2], "Contents", "Resources", "Apps"))

                        # Sync FastFlagConfiguration.json files
                        printMainMessage("Copying Configuration Files..")
                        fast_config_path = os.path.join(stored_main_app[found_platform][0], "Contents", "Resources", "FastFlagConfiguration.json")
                        if os.path.exists(fast_config_path):
                            if not ("EfazRobloxBootstrap.app" in os.getcwd()): fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = os.getcwd()
                            with open(fast_config_path, "w") as f:
                                json.dump(fastFlagConfig, f, indent=4)
                        else:
                            if not ("EfazRobloxBootstrap.app" in os.getcwd()): fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = os.getcwd()
                            with open(fast_config_path, "w") as f:
                                json.dump(fastFlagConfig, f, indent=4)

                        # Success!
                        if overwrited == True:
                            printSuccessMessage(f"Successfully updated Efaz's Roblox Bootstrap!")
                        else:
                            printSuccessMessage(f"Successfully installed Efaz's Roblox Bootstrap!")
                    else:
                        printErrorMessage("Something went wrong trying to find the application folder.")
                    shutil.rmtree(f"./Apps/EfazRobloxBootstrapMac/")
                else:
                    printErrorMessage("Something went wrong trying to find the installation folder.")
            elif main_os == "Windows":
                # Get FastFlagConfiguration.json Data
                if overwrited == True:
                    printMainMessage("Getting Configuration File Data..")
                    if os.path.exists(os.path.join(f"{stored_main_app[found_platform][0]}", "FastFlagConfiguration.json")):
                        with open(os.path.join(f"{stored_main_app[found_platform][0]}", "FastFlagConfiguration.json"), "r") as f:
                            fastFlagConfig = json.load(f)
                    else:
                        fastFlagConfig = {}
                else:
                    fastFlagConfig = {}

                # Delete Other Operating System Files
                deleted_other_os = False
                if not (disable_remove_other_operating_systems == True):
                    if os.path.exists("./Apps/EfazRobloxBootstrapMac.zip"):
                        os.remove("./Apps/EfazRobloxBootstrapMac.zip")
                        deleted_other_os = True
                    if is_x86_windows():
                        if os.path.exists("./Apps/EfazRobloxBootstrap/"):
                            shutil.rmtree("./Apps/EfazRobloxBootstrap/")
                            deleted_other_os = True
                    else:
                        if os.path.exists("./Apps/EfazRobloxBootstrap32/"):
                            shutil.rmtree("./Apps/EfazRobloxBootstrap32/")
                            deleted_other_os = True
                    if deleted_other_os == True: printMainMessage("To help save space, the script has automatically deleted files made for other operating systems!")

                # Convert All Mod Modes to Mods
                if os.path.exists("./ModModes/"):
                    printMainMessage("Converting Mod Modes to Mods..")
                    for i in os.listdir("./ModModes/"):
                        mod_mode_path = os.path.join("./ModModes/", i)
                        if os.path.isdir(mod_mode_path):
                            if not os.path.exists(f"./Mods/{i}/"):
                                os.makedirs(f"./Mods/{i}/", exist_ok=True)
                            shutil.copytree(mod_mode_path, f"./Mods/{i}/", dirs_exist_ok=True)
                    shutil.rmtree("./ModModes/")
                if os.path.exists(os.path.join(stored_main_app[found_platform][0], "ModModes")):
                    printMainMessage("Converting Mod Modes to Mods..")
                    for i in os.listdir(os.path.join(stored_main_app[found_platform][0], "ModModes")):
                        mod_mode_path = os.path.join(os.path.join(stored_main_app[found_platform][0], "ModModes"), i)
                        if os.path.isdir(mod_mode_path):
                            if not os.path.exists(os.path.join(stored_main_app[found_platform][0], "Mods", i)):
                                os.makedirs(os.path.join(stored_main_app[found_platform][0], "Mods", i), exist_ok=True)
                            shutil.copytree(mod_mode_path, os.path.join(stored_main_app[found_platform][0], "Mods", i), dirs_exist_ok=True)
                    shutil.rmtree(os.path.join(stored_main_app[found_platform][0], "ModModes"))

                # Copy Apps
                printMainMessage("Creating paths..")
                os.makedirs(stored_main_app[found_platform][0], exist_ok=True)
                printMainMessage("Installing EXE File..")
                if is_x86_windows():
                    shutil.copy(os.path.join(os.curdir, "Apps", "EfazRobloxBootstrap32", "EfazRobloxBootstrap32.exe"), stored_main_app[found_platform][1])
                    shutil.copy(os.path.join(os.curdir, "Apps", "PlayRoblox", "PlayRoblox32.exe"), os.path.join(stored_main_app[found_platform][2], "PlayRoblox.exe"))
                    shutil.copytree(os.path.join(os.curdir, "Apps", "EfazRobloxBootstrap32", "_internal"), os.path.join(stored_main_app[found_platform][0], "_internal"), dirs_exist_ok=True)
                else:
                    shutil.copy(os.path.join(os.curdir, "Apps", "EfazRobloxBootstrap", "EfazRobloxBootstrap.exe"), stored_main_app[found_platform][1])
                    shutil.copy(os.path.join(os.curdir, "Apps", "PlayRoblox", "PlayRoblox.exe"), os.path.join(stored_main_app[found_platform][2], "PlayRoblox.exe"))
                    shutil.copytree(os.path.join(os.curdir, "Apps", "EfazRobloxBootstrap", "_internal"), os.path.join(stored_main_app[found_platform][0], "_internal"), dirs_exist_ok=True)

                # Setup URL Schemes
                import winreg
                disabled_url_schemes = False
                if instant_install == False:
                    printMainMessage("Would you like to install URL Schemes?")
                    a = input("> ")
                    if not (a.lower() == "n"):
                        printMainMessage("Setting up URL Schemes..")
                        def set_url_scheme(protocol, exe_path):
                            protocol_key = r"Software\Classes\{}".format(protocol)
                            command_key = r"Software\Classes\{}\shell\open\command".format(protocol)

                            try:
                                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, protocol_key) as key:
                                    winreg.SetValue(key, "", winreg.REG_SZ, "URL:{}".format(protocol))
                                    winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, protocol)
                                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, command_key) as key:
                                    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, '"{}" "%1"'.format(exe_path))
                                printSuccessMessage(f'URL scheme "{protocol}" has been set for "{exe_path}"')
                            except Exception as e:
                                printErrorMessage(f"An error occurred: {e}")
                        set_url_scheme("efaz-bootstrap", stored_main_app[found_platform][1])
                        set_url_scheme("roblox-player", stored_main_app[found_platform][1])
                        set_url_scheme("roblox", stored_main_app[found_platform][1])
                    else:
                        disabled_url_schemes = True
                else:
                    printMainMessage("Setting up URL Schemes..")
                    def set_url_scheme(protocol, exe_path):
                        protocol_key = r"Software\Classes\{}".format(protocol)
                        command_key = r"Software\Classes\{}\shell\open\command".format(protocol)

                        try:
                            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, protocol_key) as key:
                                winreg.SetValue(key, "", winreg.REG_SZ, "URL:{}".format(protocol))
                                winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, protocol)
                            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, command_key) as key:
                                winreg.SetValueEx(key, "", 0, winreg.REG_SZ, '"{}" "%1"'.format(exe_path))
                            printSuccessMessage(f'URL scheme "{protocol}" has been set for "{exe_path}"')
                        except Exception as e:
                            printErrorMessage(f"An error occurred: {e}")
                    set_url_scheme("efaz-bootstrap", stored_main_app[found_platform][1])
                    set_url_scheme("roblox-player", stored_main_app[found_platform][1])
                    set_url_scheme("roblox", stored_main_app[found_platform][1])

                # Setup Shortcuts
                printMainMessage("Setting up shortcuts..")
                import win32com.client
                def create_shortcut(target_path, shortcut_path, working_directory=None, icon_path=None):
                    shell = win32com.client.Dispatch('WScript.Shell')
                    shortcut = shell.CreateShortcut(shortcut_path)
                    shortcut.TargetPath = target_path
                    if working_directory:
                        shortcut.WorkingDirectory = working_directory
                    if icon_path:
                        shortcut.IconLocation = icon_path
                    shortcut.save()
                create_shortcut(stored_main_app[found_platform][1], os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'), "Efaz's Roblox Bootstrap.lnk"))
                create_shortcut(stored_main_app[found_platform][1], os.path.join(os.path.join(os.path.join(os.environ['APPDATA']), 'Microsoft', 'Windows', 'Start Menu', 'Programs'), "Efaz's Roblox Bootstrap.lnk"))
                create_shortcut(os.path.join(stored_main_app[found_platform][2], "PlayRoblox.exe"), os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'), 'Play Roblox.lnk'))
                create_shortcut(os.path.join(stored_main_app[found_platform][2], "PlayRoblox.exe"), os.path.join(os.path.join(os.path.join(os.environ['APPDATA']), 'Microsoft', 'Windows', 'Start Menu', 'Programs'), 'Play Roblox.lnk'))

                # Copy App Resources
                printMainMessage("Copying App Resources..")
                if os.path.exists(stored_main_app[found_platform][1]):
                    shutil.copytree(os.curdir, stored_main_app[found_platform][0], dirs_exist_ok=True, ignore=ignore_files_func)

                    # Handle Existing Configuration Files
                    printMainMessage("Copying Configuration Files..")
                    if os.path.exists(os.path.join(f"{stored_main_app[found_platform][0]}", "FastFlagConfiguration.json")):
                        if disabled_url_schemes == True:
                            fastFlagConfig["EFlagDisableURLSchemeInstall"] = True
                        else:
                            fastFlagConfig["EFlagDisableURLSchemeInstall"] = False
                        if not ("/Local/EfazRobloxBootstrap/" in os.getcwd()): fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = os.getcwd()
                        with open(os.path.join(f"{stored_main_app[found_platform][0]}", "FastFlagConfiguration.json"), "w") as f:
                            json.dump(fastFlagConfig, f, indent=4)
                    else:
                        if disabled_url_schemes == True:
                            fastFlagConfig["EFlagDisableURLSchemeInstall"] = True
                        else:
                            fastFlagConfig["EFlagDisableURLSchemeInstall"] = False
                        if not ("/Local/EfazRobloxBootstrap/" in os.getcwd()): fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = os.getcwd()
                        with open(os.path.join(f"{stored_main_app[found_platform][0]}", "FastFlagConfiguration.json"), "w") as f:
                            json.dump(fastFlagConfig, f, indent=4)

                    # Remove Apps Folder in /Contents/Resources/
                    printMainMessage("Removing Apps Folder in /Contents/Resources/ to save space.")
                    if os.path.exists(os.path.join(stored_main_app[found_platform][0], "Apps")):
                        shutil.rmtree(os.path.join(stored_main_app[found_platform][0], "Apps"))
                    if os.path.exists(os.path.join(stored_main_app[found_platform][1], "Apps")):
                        shutil.rmtree(os.path.join(stored_main_app[found_platform][1], "Apps"))
                    if os.path.exists(os.path.join(stored_main_app[found_platform][2], "Apps")):
                        shutil.rmtree(os.path.join(stored_main_app[found_platform][2], "Apps"))

                    # Mark Installation in Windows
                    printMainMessage("Marking Program Installation into Windows..")
                    app_key = "Software\\EfazRobloxBootstrap"
                    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, app_key) as key:
                        winreg.SetValueEx(key, "InstallPath", 0, winreg.REG_SZ, stored_main_app[found_platform][0])
                        winreg.SetValueEx(key, "Installed", 0, winreg.REG_DWORD, 1)

                    registry_path = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\EfazRobloxBootstrap"
                    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, registry_path) as key:
                        winreg.SetValueEx(key, "UninstallString", 0, winreg.REG_SZ, f"py {os.path.join(stored_main_app[found_platform][0], "Uninstall.py")}")
                        winreg.SetValueEx(key, "DisplayName", 0, winreg.REG_SZ, "Efaz's Roblox Bootstrap")
                        winreg.SetValueEx(key, "DisplayVersion", 0, winreg.REG_SZ, "1.2.0")
                        winreg.SetValueEx(key, "DisplayIcon", 0, winreg.REG_SZ, os.path.join(stored_main_app[found_platform][0], "AppIcon.ico"))

                    # Success!
                    if overwrited == True:
                        printSuccessMessage(f"Successfully updated Efaz's Roblox Bootstrap!")
                    else:
                        printSuccessMessage(f"Successfully installed Efaz's Roblox Bootstrap!")
                else:
                    printErrorMessage("Something went wrong trying to find the installation folder.")
            else:
                printErrorMessage("Efaz's Roblox Bootstrap is only supported for macOS or Windows.")
        else:
            printErrorMessage("There was an issue while finding the Apps folder for installation.")
    if silent_mode == True:
        install()
    else:
        if overwrited == True:
            printWarnMessage("--- Updater ---")
        else:
            printWarnMessage("--- Installer ---")
        if instant_install == True:
            install()
        else:
            if overwrited == True:
                printMainMessage("Do you want to update Efaz's Roblox Bootstrap? (This will reupdate all files based on this Installation folder.) (y/n)")
            else:
                printMainMessage("Do you want to install Efaz's Roblox Bootstrap into your system? (This will add the app to your Applications folder.) (y/n)")
        res = input("> ")
        if isYes(res) == True:
            install()
            input("> ")
    sys.exit(0)
else:
    class EfazRobloxBootstrapNotModule(Exception):
        def __init__(self):            
            super().__init__("Efaz's Roblox Bootstrap is only a runable instance, not a module.")
    class EfazRobloxBootstrapInstallerNotModule(Exception):
        def __init__(self):            
            super().__init__("The installer for Efaz's Roblox Bootstrap is only a runable instance, not a module.")
    class EfazRobloxBootstrapLoaderNotModule(Exception):
        def __init__(self):            
            super().__init__("The loader for Efaz's Roblox Bootstrap is only a runable instance, not a module.")
    raise EfazRobloxBootstrapInstallerNotModule()