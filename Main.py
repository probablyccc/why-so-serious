import os
import shutil
import json
import sys
import platform
import datetime
import importlib.util
import subprocess
import threading
import time
from urllib.parse import unquote
import RobloxFastFlagsInstaller

class pip:
    def install(self, packages: list[str]):
        for i in packages:
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", i])
    def uninstall(self, packages: list[str]):
        for i in packages:
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "uninstall", i])
    def installed(self, packages: list[str]):
        installed = {}
        all_installed = True
        for i in packages:
            import importlib
            try:
                a = importlib.import_module(i)
                if a:
                    installed[i] = True
                else:
                    installed[i] = False
                    all_installed = False
            except Exception as e:
                installed[i] = False
                all_installed = False
        installed["all"] = all_installed
        return installed
    def pythonInstalled(self):
        import platform
        import os
        import subprocess
        import glob
        ma_os = platform.system()
        if ma_os == "Darwin":
            paths = [
                "/usr/local/bin/python*",
                "/Library/Frameworks/Python.framework/Versions/*/bin/python*",
                "~/Library/Python/*/bin/python*"
            ]
            for path_pattern in paths:
                for path in glob.glob(path_pattern):
                    if os.path.isfile(path):
                        return True
            return False
        elif ma_os == "Windows":
            paths = [
                os.path.expandvars(r'%LOCALAPPDATA%\\Programs\\Python\\Python*'),
                os.path.expandvars(r'%LOCALAPPDATA%\\Programs\\Python\\Python*\\python.exe'),
                os.path.expandvars(r'%PROGRAMFILES%\\Python*\\python.exe'),
                os.path.expandvars(r'%PROGRAMFILES(x86)%\\Python*\\python.exe')
            ]
            for path_pattern in paths:
                for path in glob.glob(path_pattern):
                    if os.path.isfile(path):
                        return True
            return False
    def pythonInstall(self):
        import platform
        import subprocess
        import tempfile

        ma_os = platform.system()
        if ma_os == "Darwin":
            url = "https://www.python.org/ftp/python/3.12.5/python-3.12.5-macos11.pkg"
            pkg_file_path = tempfile.mktemp(suffix=".pkg")
            result = subprocess.run(["curl", "-o", pkg_file_path, url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)            
            if result.returncode == 0:
                subprocess.run(["open", pkg_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                print(f"Python installer has been executed: {pkg_file_path}")
            else:
                print("Failed to download Python installer.")
        elif ma_os == "Windows":
            url = "https://www.python.org/ftp/python/3.12.5/python-3.12.5.exe"
            exe_file_path = tempfile.mktemp(suffix=".exe")
            result = subprocess.run(["curl", "-o", exe_file_path, url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)            
            if result.returncode == 0:
                subprocess.run(["open", exe_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                print(f"Python installer has been executed: {exe_file_path}")
            else:
                print("Failed to download Python installer.")

if __name__ == "__main__":
    main_os = platform.system()
    windows_dir = os.path.join(f"{os.getenv('LOCALAPPDATA')}", "Roblox")

    stored_content_folder_destinations = {
        "Darwin": "/Applications/Roblox.app/Contents/Resources/"
    }
    stored_font_folder_destinations = {
        "Darwin": f"{stored_content_folder_destinations['Darwin']}content/fonts/"
    }
    stored_robux_folder_destinations = {
        "Darwin": f"{stored_content_folder_destinations['Darwin']}content/textures/ui/common/"
    }
    handler = RobloxFastFlagsInstaller.Main()
    loadedJSON = True
    makeAnotherRoblox = False
    currentVersion = {"version": "1.1.5"}
    given_args = list(filter(None, sys.argv))

    with open("FastFlagConfiguration.json", "r") as f:
        try:
            fastFlagConfig = json.loads(f.read())
        except Exception as e:
            loadedJSON = False

    def printMainMessage(mes):
        print(f"\033[38;5;255m{mes}\033[0m")

    def printErrorMessage(mes):
        print(f"\033[38;5;196m{mes}\033[0m")

    def printSuccessMessage(mes):
        print(f"\033[38;5;82m{mes}\033[0m")

    def printWarnMessage(mes):
        print(f"\033[38;5;202m{mes}\033[0m")

    def printYellowMessage(mes):
        print(f"\033[38;5;226m{mes}\033[0m")

    def printDebugMessage(mes):
        if loadedJSON:
            if fastFlagConfig.get("EFlagEnableDebugMode"):
                printYellowMessage(mes)

    def isYes(text):
        return text.lower() == "y" or text.lower() == "yes"
    
    def isNo(text):
        return text.lower() == "n" or text.lower() == "no"
    
    def isRequestClose(text):
        return text.lower() == "exit" or text.lower() == "exit()"
    
    def copyFile(pa, de):
        if os.path.exists(pa):
            if os.path.exists("./ExportMode/"):
                destination_dir = f"./ExportMode{os.path.dirname(de)}"
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                    printDebugMessage(f"Created directory: {destination_dir}")
                destination_path = f"./ExportMode{de}"
                a = shutil.copy(pa, destination_path)
            a = shutil.copy(pa, de)
            printDebugMessage(f"Copied File: {pa} => {de}")
            return a
        else:
            printDebugMessage(f"File not found: {pa}")
            return None
    
    def readJSONFile(path, listExpected=False):
        with open(path, "r") as f:
            try:
                main_content = json.load(f)
                if listExpected == True:
                    if type(main_content) is list:
                        return main_content
                    else:
                        return None
                else:
                    if type(main_content) is dict:
                        return main_content
                    else:
                        return None
            except Exception as e:
                return None
        return None
    
    os.system("cls" if os.name == "nt" else "clear")
    if main_os == "Windows":
        printWarnMessage("-----------")
        printWarnMessage("Welcome to Efaz's Roblox Bootstrap!")
    elif main_os == "Darwin":
        printWarnMessage("-----------")
        printWarnMessage("Welcome to Efaz's Roblox Bootstrap!")
    else:
        printErrorMessage("Please run this script on macOS/Windows.")
        exit()
    printWarnMessage("Made by Efaz from efaz.dev!")
    printWarnMessage(f"v{currentVersion['version']}")
    printWarnMessage("-----------")
    printMainMessage("Getting Roblox Version..")
    if main_os == "Windows":
        stored_content_folder_destinations["Windows"] = f"{handler.getRobloxInstallFolder()}\\"
        stored_font_folder_destinations["Windows"] = f"{stored_content_folder_destinations['Windows']}content\\fonts\\"
        stored_robux_folder_destinations["Windows"] = f"{stored_content_folder_destinations['Windows']}content\\textures\\ui\\common\\"
        if not stored_font_folder_destinations["Windows"]:
            printErrorMessage("Please install Roblox from the Roblox website!")
            exit()
    printMainMessage("Determining System OS..")
    if main_os == "Windows":
        found_platform = "Windows"
    elif main_os == "Darwin":
        found_platform = "Darwin"
    else:
        printErrorMessage("Please run this script on macOS/Windows.")
        exit()

    if main_os == "Darwin":
        if os.path.exists("/Applications/EfazRobloxBootstrap.app/Contents/Resources/URLSchemeExchange"):
            with open("/Applications/EfazRobloxBootstrap.app/Contents/Resources/URLSchemeExchange", "r") as f:
                filtered_args = f.read()
            if (("roblox-player:" in filtered_args) or ("roblox:" in filtered_args)) and not (loadedJSON == True and fastFlagConfig.get("EFlagEnableDebugMode") == True):
                if fastFlagConfig.get("EFlagEnableDebugMode"): printDebugMessage("Moved command execution to file args to prevent user from showing the command with private info.")
            given_args = ["Main.py", filtered_args]
            os.remove("/Applications/EfazRobloxBootstrap.app/Contents/Resources/URLSchemeExchange")

    def handleOption1():
        printWarnMessage("--- Continue to Roblox ---")
        printMainMessage("Continuing to next stage!")

    def handleOption2():
        printWarnMessage("--- Multiple Instances ---")
        if main_os == "Windows":
            printErrorMessage("Multiple Roblox Instances on Efaz's Roblox Bootstrap is not available for Windows. [Currently, only for macOS.]")
            input("> ")
            exit()
        elif main_os == "Darwin":
            global makeAnotherRoblox
            makeAnotherRoblox = True
            printMainMessage("Continuing to next stage!")

    def handleOption3():
        printWarnMessage("--- Running Installer ---")
        subprocess.run(args=[sys.executable, "RobloxFastFlagsInstaller.py"])

        global loadedJSON
        loadedJSON = True
        with open("FastFlagConfiguration.json", "r") as f:
            try:
                fastFlagConfig = json.loads(f.read())
            except Exception as e:
                loadedJSON = False

        if (fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir") and os.path.exists(fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir"))):
            if main_os == "Windows":
                if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json'):
                    with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json', "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                    printSuccessMessage("Successfully synced Bootstrap Settings!")
                else:
                    printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")
            elif main_os == "Darwin":
                if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json'):
                    with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json', "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                    printSuccessMessage("Successfully synced Bootstrap Settings!")
                else:
                    printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")

    def handleOption4():
        printWarnMessage("--- Settings ---")
        global fastFlagConfig
        printMainMessage("Would you like to remove the Builder Font and use the old one? (y/n)")
        a = input("> ")
        if isYes(a) == True:
            fastFlagConfig["EFlagRemoveBuilderFont"] = True
            printDebugMessage("User selected: True")
        elif isNo(a) == True:
            fastFlagConfig["EFlagRemoveBuilderFont"] = False
            printDebugMessage("User selected: False")

        printMainMessage("Would you like to use a Mod Mode? (y/n)")
        b = input("> ")
        if isYes(b) == True:
            mode_jsons = {}
            fastFlagConfig["EFlagEnableModModes"] = True
            def scan_name(a):
                if main_os == "Windows":
                    if os.path.exists(f"{os.path.curdir}\\ModModes\\{a}\\") and os.path.exists(f"{os.path.curdir}\\ModModes\\{a}\\Manifest.json"):
                        return True
                    else:
                        return False
                elif main_os == "Darwin":
                    if os.path.exists(f"{os.path.curdir}/ModModes/{a}/") and os.path.exists(f"{os.path.curdir}/ModModes/{a}/Manifest.json"):
                        return True
                    else:
                        return False
            def getName():
                unfiltered_got_mode = []
                got_mode = []
                for i in os.listdir("./ModModes/"):
                    if os.path.isdir(f"./ModModes/{i}/") and os.path.exists(f"./ModModes/{i}/Manifest.json"):
                        unfiltered_got_mode.append(i)
                printWarnMessage("Select the number that is associated with the mod you want to use.")
                unfiltered_got_mode = sorted(unfiltered_got_mode)
                count = 1
                for i in unfiltered_got_mode:
                    res_json = readJSONFile(f"./ModModes/{i}/Manifest.json")
                    if res_json:
                        final_vers = "1.0.0"
                        if res_json.get("version"):
                            if type(res_json.get("version")) is str and len(res_json.get("version")) < 10:
                                final_vers = res_json.get("version")
                        got_mode.append(i)
                        mode_jsons[i] = res_json
                        if res_json.get("name") == i:
                            printMainMessage(f"[{str(count)}] = {i} [v{final_vers}]")
                        elif type(res_json.get("name")) is str:
                            printMainMessage(f"[{str(count)}] = {res_json.get('name')} [v{final_vers}] [{i}]")
                        else:
                            printMainMessage(f"[{str(count)}] = {i} [v{final_vers}]")
                    count += 1
                if main_os == "Darwin":
                    printYellowMessage("[Also, if you just added a new mod folder into the ModModes folder, please rerun Install.py in order for it to seen.]")
                a = input("> ")
                if a.isnumeric():
                    c = int(a)-1
                    if c < len(got_mode) and c >= 0:
                        if got_mode[c]:
                            b = got_mode[c]
                            if scan_name(b) == True:
                                return b
                            else:
                                printDebugMessage("Directory is not valid.")
                                return "Original"
                        else:
                            printDebugMessage("User gave a number which is somehow not on the list..?")
                            return "Original"
                    else:
                        printDebugMessage("User gave a number which is out of reach.")
                        return "Original"
                else:
                    printDebugMessage("User gave a response which is not a number.")
                    return "Original"
            set_mod_mode = getName()
            if not (fastFlagConfig.get("EFlagSelectedModMode") == None or fastFlagConfig.get("EFlagSelectedModMode") == "Original") and set_mod_mode == "Original":
                fastFlagConfig["EFlagModModeAllowedDetectments"] = []
                fastFlagConfig["EFlagEnableModModeScripts"] = False
                printMainMessage("It seems like you have defaulted the current mod mode to Original! Would you like to reinstall Roblox to clear previous mods?")
                a = input("> ")
                if isYes(a) == True:
                    handler.installRoblox()
            elif os.path.exists(os.path.join(os.path.curdir, "ModModes", set_mod_mode, "Manifest.json")):
                res_json = readJSONFile(f"./ModModes/{set_mod_mode}/Manifest.json")
                if res_json:
                    if (not (fastFlagConfig.get("EFlagAllowActivityTracking") == True) or (fastFlagConfig.get("EFlagAllowActivityTracking") == None)) and (res_json.get("mod_script") == True):
                        printMainMessage("Would you like to allow Activity Tracking on the Roblox client? (y/n)")
                        printMainMessage("This will allow features like:")
                        printMainMessage("- Server Locations")
                        printMainMessage("- Discord Webhook")
                        printMainMessage("- BloxstrapRPC")
                        printMainMessage("- Discord Presence")
                        printMainMessage("- Mod Mode Scripts")
                        d = input("> ")
                        if isYes(d) == True:
                            fastFlagConfig["EFlagAllowActivityTracking"] = True
                            printDebugMessage("User selected: True")
                        elif isNo(d) == True:
                            fastFlagConfig["EFlagAllowActivityTracking"] = False
                            printDebugMessage("User selected: False")
                    if res_json.get("mod_script") == True and os.path.exists(os.path.join(os.path.curdir, "ModModes", set_mod_mode, "ModScript.py")) and fastFlagConfig.get("EFlagAllowActivityTracking") == True:
                        printMainMessage("It seems like this mod mode contains a script enabled. Would you like to enable it with Activity Tracking? (y/n)")
                        if type(res_json.get("mod_script_requirements")) is list:
                            printMainMessage("You will enable the following for this item: ")
                            for i in res_json.get("mod_script_requirements"):
                                if type(i) is str and handler.robloxInstanceInfoNames.get(i):
                                    mai = handler.robloxInstanceInfoNames.get(i)
                                    if "Allow detecting every Roblox event" in mai:
                                        printErrorMessage(f"- {handler.robloxInstanceInfoNames.get(i)}")
                                    elif "Allow detecting when Roblox HttpResponses are ran" in mai or "Allow detecting when Unknown Roblox Handlers are detected" in mai:
                                        printWarnMessage(f"- {handler.robloxInstanceInfoNames.get(i)}")
                                    elif "Allow getting Job ID, Place ID and Roblox IP" in mai or "Allow detecting when loading " in mai:
                                        printYellowMessage(f"- {handler.robloxInstanceInfoNames.get(i)}")
                                    else:
                                        printMainMessage(f"- {handler.robloxInstanceInfoNames.get(i)}")
                                else:
                                    printErrorMessage(f"- Unknown Requirement")
                        printWarnMessage("PLEASE CHECK THE SCRIPT BEFORE ENABLING! DON'T ENABLE IF YOU DON'T KNOW WHAT YOU'RE DOING!!")
                        a = input("> ")
                        if isYes(a) == True:
                            if type(res_json.get("mod_script_requirements")) is list:
                                fastFlagConfig["EFlagModModeAllowedDetectments"] = res_json.get("mod_script_requirements")
                            else:
                                fastFlagConfig["EFlagModModeAllowedDetectments"] = []
                            fastFlagConfig["EFlagEnableModModeScripts"] = True
                        else:
                            fastFlagConfig["EFlagModModeAllowedDetectments"] = []
                            fastFlagConfig["EFlagEnableModModeScripts"] = False
                    else:
                        fastFlagConfig["EFlagModModeAllowedDetectments"] = []
                        fastFlagConfig["EFlagEnableModModeScripts"] = False
                else:
                    fastFlagConfig["EFlagModModeAllowedDetectments"] = []
                    fastFlagConfig["EFlagEnableModModeScripts"] = False
            else:
                fastFlagConfig["EFlagModModeAllowedDetectments"] = []
                fastFlagConfig["EFlagEnableModModeScripts"] = False
            fastFlagConfig["EFlagSelectedModMode"] = set_mod_mode
            printSuccessMessage(f"Set mod mode: {set_mod_mode}")
        elif isNo(b) == True:
            fastFlagConfig["EFlagEnableModModes"] = False
            printDebugMessage("User selected: False")


        printMainMessage("Would you like to change the background of the Avatar Editor? (y/n)")
        c = input("> ")
        if isYes(c) == True:
            fastFlagConfig["EFlagEnableChangeAvatarEditorBackground"] = True
            def scan_name(a):
                if main_os == "Windows":
                    if os.path.exists(f"{os.path.curdir}\\AvatarEditorMaps\\{a}\\AvatarBackground.rbxl"):
                        return True
                    else:
                        return False
                elif main_os == "Darwin":
                    if os.path.exists(f"{os.path.curdir}/AvatarEditorMaps/{a}/AvatarBackground.rbxl"):
                        return True
                    else:
                        return False
            def getName():
                got_backgrounds = []
                for i in os.listdir("./AvatarEditorMaps/"):
                    if os.path.isdir(f"./AvatarEditorMaps/{i}/"):
                        got_backgrounds.append(i)
                printWarnMessage("Select the number that is associated with the map you want to use.")
                got_backgrounds = sorted(got_backgrounds)
                count = 1
                for i in got_backgrounds:
                    printMainMessage(f"[{str(count)}] = {i}")
                    count += 1
                if main_os == "Darwin":
                    printYellowMessage("[Please know specific maps may not support macOS.]")
                    printYellowMessage("[Also, if you just added a new map folder into the AvatarEditorMaps folder, please rerun Install.py in order for it to seen.]")
                a = input("> ")
                if a.isnumeric():
                    c = int(a)-1
                    if c < len(got_backgrounds) and c >= 0:
                        if got_backgrounds[c]:
                            b = got_backgrounds[c]
                            if scan_name(b) == True:
                                return b
                            else:
                                printDebugMessage("Directory is not valid.")
                                return "Original"
                        else:
                            printDebugMessage("User gave a number which is somehow not on the list..?")
                            return "Original"
                    else:
                        printDebugMessage("User gave a number which is out of reach.")
                        return "Original"
                else:
                    printDebugMessage("User gave a response which is not a number.")
                    return "Original"
            set_avatar_editor_location = getName()
            fastFlagConfig["EFlagAvatarEditorBackground"] = set_avatar_editor_location
            printSuccessMessage(f"Set avatar background: {set_avatar_editor_location}")
        elif isNo(c) == True:
            fastFlagConfig["EFlagEnableChangeAvatarEditorBackground"] = False
            printDebugMessage("User selected: False")

        printMainMessage("Would you like to change the Roblox cursor? (y/n)")
        c = input("> ")
        if isYes(c) == True:
            fastFlagConfig["EFlagEnableChangeCursor"] = True
            def scan_name(a):
                if main_os == "Windows":
                    if os.path.exists(f"{os.path.curdir}\\Cursors\\{a}\\ArrowCursor.png") and os.path.exists(f"{os.path.curdir}\\Cursors\\{a}\\ArrowFarCursor.png"):
                        return True
                    else:
                        return False
                elif main_os == "Darwin":
                    if os.path.exists(f"{os.path.curdir}/Cursors/{a}/ArrowCursor.rbxl") and os.path.exists(f"{os.path.curdir}/Cursors/{a}/ArrowFarCursor.rbxl"):
                        return True
                    else:
                        return False
            def getName():
                got_cursors = []
                for i in os.listdir("./Cursors/"):
                    if os.path.isdir(f"./Cursors/{i}/"):
                        got_cursors.append(i)
                got_cursors = sorted(got_cursors)
                printWarnMessage("Select the number that is associated with the cursor you want to use.")
                count = 1
                for i in got_cursors:
                    printMainMessage(f"[{str(count)}] = {i}")
                    count += 1
                if main_os == "Darwin":
                    printYellowMessage("[Also, if you just added a new cursor folder into the Cursors folder, please rerun Install.py in order for it to seen.]")
                a = input("> ")
                if a.isnumeric():
                    c = int(a)-1
                    if c < len(got_cursors) and c >= 0:
                        if got_cursors[c]:
                            b = got_cursors[c]
                            if scan_name(b) == True:
                                return b
                            else:
                                printDebugMessage("Directory is not valid.")
                                return "Original"
                        else:
                            printDebugMessage("User gave a number which is somehow not on the list..?")
                            return "Original"
                    else:
                        printDebugMessage("User gave a number which is out of reach.")
                        return "Original"
                else:
                    printDebugMessage("User gave a response which is not a number.")
                    return "Original"
            set_cursor_location = getName()
            fastFlagConfig["EFlagSelectedCursor"] = set_cursor_location
            printSuccessMessage(f"Set cursor folder: {set_cursor_location}")
        elif isNo(c) == True:
            fastFlagConfig["EFlagEnableChangeCursor"] = False
            printDebugMessage("User selected: False")

        printMainMessage("Would you like to change the Roblox logo? (y/n)")
        c = input("> ")
        if isYes(c) == True:
            fastFlagConfig["EFlagEnableChangeBrandIcons"] = True
            def scan_name(a):
                if main_os == "Windows":
                    if os.path.exists(f"{os.path.curdir}\\RobloxBrand\\{a}\\AppIcon.icns"):
                        return True
                    else:
                        return False
                elif main_os == "Darwin":
                    if os.path.exists(f"{os.path.curdir}/RobloxBrand/{a}/AppIcon.icns"):
                        return True
                    else:
                        return False
            def getName():
                got_icons = []
                for i in os.listdir("./RobloxBrand/"):
                    if os.path.isdir(f"./RobloxBrand/{i}/"):
                        got_icons.append(i)
                got_icons = sorted(got_icons)
                printWarnMessage("Select the number that is associated with the icon you want to use.")
                count = 1
                for i in got_icons:
                    printMainMessage(f"[{str(count)}] = {i}")
                    count += 1
                if main_os == "Darwin":
                    printYellowMessage("[Also, if you just added a new icon folder into the RobloxBrand folder, please rerun Install.py in order for it to seen.]")
                a = input("> ")
                if a.isnumeric():
                    c = int(a)-1
                    if c < len(got_icons) and c >= 0:
                        if got_icons[c]:
                            b = got_icons[c]
                            if scan_name(b) == True:
                                return b
                            else:
                                printDebugMessage("Directory is not valid.")
                                return "Original"
                        else:
                            printDebugMessage("User gave a number which is somehow not on the list..?")
                            return "Original"
                    else:
                        printDebugMessage("User gave a number which is out of reach.")
                        return "Original"
                else:
                    printDebugMessage("User gave a response which is not a number.")
                    return "Original"
            set_app_icon_location = getName()
            fastFlagConfig["EFlagSelectedBrandLogo"] = set_app_icon_location
            printSuccessMessage(f"Set logo folder: {set_app_icon_location}")
        elif isNo(c) == True:
            fastFlagConfig["EFlagEnableChangeBrandIcons"] = False
            printDebugMessage("User selected: False")

        printMainMessage("Would you like to change the Roblox death sound? (y/n)")
        c = input("> ")
        if isYes(c) == True:
            fastFlagConfig["EFlagEnableChangeDeathSound"] = True
            def scan_name(a):
                if main_os == "Windows":
                    if os.path.exists(f"{os.path.curdir}\\DeathSounds\\{a}"):
                        return True
                    else:
                        return False
                elif main_os == "Darwin":
                    if os.path.exists(f"{os.path.curdir}/DeathSounds/{a}"):
                        return True
                    else:
                        return False
            def getName():
                got_sounds = []
                for i in os.listdir("./DeathSounds/"):
                    if os.path.isfile(f"./DeathSounds/{i}") and i.endswith(".ogg"):
                        got_sounds.append(i)
                got_sounds = sorted(got_sounds)
                printWarnMessage("Select the number that is associated with the sound you want to use.")
                count = 1
                for i in got_sounds:
                    printMainMessage(f"[{str(count)}] = {i}")
                    count += 1
                if main_os == "Darwin":
                    printYellowMessage("[Also, if you just added a new sound file into the DeathSounds folder, please rerun Install.py in order for it to seen.]")
                a = input("> ")
                if a.isnumeric():
                    c = int(a)-1
                    if c < len(got_sounds) and c >= 0:
                        if got_sounds[c]:
                            b = got_sounds[c]
                            if scan_name(b) == True:
                                return b
                            else:
                                printDebugMessage("Directory is not valid.")
                                return "New"
                        else:
                            printDebugMessage("User gave a number which is somehow not on the list..?")
                            return "New"
                    else:
                        printDebugMessage("User gave a number which is out of reach.")
                        return "New"
                else:
                    printDebugMessage("User gave a response which is not a number.")
                    return "New"
            set_death_sound = getName()
            fastFlagConfig["EFlagSelectedDeathSound"] = set_death_sound
            printSuccessMessage(f"Set death sound: {set_death_sound}")
        elif isNo(c) == True:
            fastFlagConfig["EFlagEnableChangeDeathSound"] = False
            printDebugMessage("User selected: False")

        if main_os == "Darwin":
            printMainMessage("Would you like to allow duplication of Roblox Clients on default? (y/n)")
            c = input("> ")
            if isYes(c) == True:
                fastFlagConfig["EFlagEnableDuplicationOfClients"] = True
                printDebugMessage("User selected: True")
                printYellowMessage("Notes to keep track of:")
                printYellowMessage("1. Make sure all currently open instances are fully loaded in a game before going to an another account.")
                printYellowMessage("2. Use only the bootstrap to load Roblox since macOS will try to validate a check and fail.")
            elif isNo(c) == True:
                fastFlagConfig["EFlagEnableDuplicationOfClients"] = False
                printDebugMessage("User selected: False")

        printMainMessage("Would you like to allow Activity Tracking on the Roblox client? (y/n)")
        printMainMessage("This will allow features like:")
        printMainMessage("- Server Locations")
        printMainMessage("- Discord Webhook")
        printMainMessage("- BloxstrapRPC")
        printMainMessage("- Discord Presence")
        printMainMessage("- Mod Mode Scripts")
        d = input("> ")
        if isYes(d) == True:
            fastFlagConfig["EFlagAllowActivityTracking"] = True
            printDebugMessage("User selected: True")
        elif isNo(d) == True:
            fastFlagConfig["EFlagAllowActivityTracking"] = False
            printDebugMessage("User selected: False")

        if not (fastFlagConfig.get("EFlagAllowActivityTracking") == False):
            printMainMessage("Would you like to enable Server Locations? (y/n)")
            d = input("> ")
            if isYes(d) == True:
                fastFlagConfig["EFlagNotifyServerLocation"] = True
                printDebugMessage("User selected: True")
            elif isNo(d) == True:
                fastFlagConfig["EFlagNotifyServerLocation"] = False
                printDebugMessage("User selected: False")

            printMainMessage("Would you like to enable Discord RPC? (extra modules may be installed when said yes) (y/n)")
            d = input("> ")
            if isYes(d) == True:
                fastFlagConfig["EFlagEnableDiscordRPC"] = True
                try:
                    from DiscordPresenceHandler import Presence
                    import requests
                except Exception as e:
                    pip().install(["pypresence", "requests"])
                    from DiscordPresenceHandler import Presence
                    import requests
                    printSuccessMessage("Successfully installed presence modules!")
                printDebugMessage("User selected: True")
                printMainMessage("Would you like to enable joining from your Discord profile? (Everyone will be allowed to join depending on type of server.)")
                d = input("> ")
                if isYes(d) == True:
                    fastFlagConfig["EFlagEnableDiscordRPCJoining"] = True
                    printDebugMessage("User selected: True")
                elif isNo(d) == True:
                    fastFlagConfig["EFlagEnableDiscordRPCJoining"] = False
                    printDebugMessage("User selected: False")
            elif isNo(d) == True:
                fastFlagConfig["EFlagEnableDiscordRPCJoining"] = False
                fastFlagConfig["EFlagEnableDiscordRPC"] = False
                printDebugMessage("User selected: False")

            if fastFlagConfig.get("EFlagEnableDiscordRPC") == True:
                printMainMessage("Would you like to enable games to use the Bloxstrap SDK? (y/n)")
                d = input("> ")
                if isYes(d) == True:
                    fastFlagConfig["EFlagAllowBloxstrapSDK"] = True
                    printDebugMessage("User selected: True")
                elif isNo(d) == True:
                    fastFlagConfig["EFlagAllowBloxstrapSDK"] = False
                    printDebugMessage("User selected: False")

                printMainMessage("Would you like to enable access to private servers you connect to from Discord Presences? (users may be able to join or not) (y/n)")
                d = input("> ")
                if isYes(d) == True:
                    fastFlagConfig["EFlagAllowPrivateServerJoining"] = True
                    printDebugMessage("User selected: True")
                elif isNo(d) == True:
                    fastFlagConfig["EFlagAllowPrivateServerJoining"] = False
                    printDebugMessage("User selected: False")

            printMainMessage("Would you like to use a Discord Webhook? (link required) (y/n)")
            d = input("> ")
            if isYes(d) == True:
                fastFlagConfig["EFlagUseDiscordWebhook"] = True
                try:
                    import requests
                except Exception as e:
                    pip().install(["requests"])
                    import requests
                printDebugMessage("User selected: True")
                printMainMessage("Please enter your Discord Webhook Link here (https://discord.com/api/webhooks/XXXXXXX/XXXXXXX): ")
                d = input("> ")
                if d.startswith("https://discord.com/api/webhooks/"):
                    printDebugMessage("URL passed test.")
                    fastFlagConfig["EFlagDiscordWebhookURL"] = d
                    printMainMessage("Enter your Discord User ID (you may need Developer Mode in order to copy):")
                    d = input("> ")
                    if d.isnumeric():
                        fastFlagConfig["EFlagDiscordWebhookUserId"] = d
                        printMainMessage("When should this Discord Webhook be notified?")
                        printMainMessage("It should be notified when I join a Roblox server. (y/n)")
                        d = input("> ")
                        if isYes(d) == True:
                            fastFlagConfig["EFlagDiscordWebhookConnect"] = True
                            printDebugMessage("User selected: True")
                        elif isNo(d) == True:
                            fastFlagConfig["EFlagDiscordWebhookConnect"] = False
                            printDebugMessage("User selected: False")
                        printMainMessage("It should be notified when I disconnect from a server. (y/n)")
                        d = input("> ")
                        if isYes(d) == True:
                            fastFlagConfig["EFlagDiscordWebhookDisconnect"] = True
                            printDebugMessage("User selected: True")
                        elif isNo(d) == True:
                            fastFlagConfig["EFlagDiscordWebhookDisconnect"] = False
                            printDebugMessage("User selected: False")
                else:
                    fastFlagConfig["EFlagUseDiscordWebhook"] = False
                    printErrorMessage("The provided webhook link is not a valid format.")
            elif isNo(d) == True:
                fastFlagConfig["EFlagUseDiscordWebhook"] = False
                printDebugMessage("User selected: False")

        printMainMessage("Would you like to enable Debug Mode? (y/n)")
        printYellowMessage("[WARNING! This will expose information like login to Roblox.]")
        printYellowMessage("[DO NOT EVER ENABLE IF SOMEONE TOLD YOU SO OR YOU USUALLY RECORD!!]")
        d = input("> ")
        if isYes(d) == True:
            fastFlagConfig["EFlagEnableDebugMode"] = True
            printDebugMessage("User selected: True")
        elif isNo(d) == True:
            fastFlagConfig["EFlagEnableDebugMode"] = False
            printDebugMessage("User selected: False")

        if fastFlagConfig.get("EFlagEnableDebugMode") == True:
            printMainMessage("Would you like to print unhandled Roblox client events? (y/n)")
            d = input("> ")
            if isYes(d) == True:
                fastFlagConfig["EFlagAllowFullDebugMode"] = True
                printDebugMessage("User selected: True")
            elif isNo(d) == True:
                fastFlagConfig["EFlagAllowFullDebugMode"] = False
                printDebugMessage("User selected: False")

        printMainMessage("Would you like to reinstall a fresh copy of Roblox every launch? (y/n)")
        d = input("> ")
        if isYes(d) == True:
            fastFlagConfig["EFlagFreshCopyRoblox"] = True
            printDebugMessage("User selected: True")
        elif isNo(d) == True:
            fastFlagConfig["EFlagFreshCopyRoblox"] = False
            printDebugMessage("User selected: False")

        printMainMessage("Would you like to skip the Bootstrap Start UI in the future? (y/n)")
        d = input("> ")
        if isYes(d) == True:
            fastFlagConfig["EFlagSkipEfazRobloxBootstrapPromptUI"] = True
            printDebugMessage("User selected: True")
        elif isNo(d) == True:
            fastFlagConfig["EFlagSkipEfazRobloxBootstrapPromptUI"] = False
            printDebugMessage("User selected: False")

        printMainMessage("Would you like to disable Bootstrap Update Checks? (y/n)")
        d = input("> ")
        if isYes(d) == True:
            fastFlagConfig["EFlagDisableBootstrapChecks"] = True
            printDebugMessage("User selected: True")
        elif isNo(d) == True:
            fastFlagConfig["EFlagDisableBootstrapChecks"] = False
            printDebugMessage("User selected: False")

        if (fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir") and os.path.exists(fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir"))):
            if main_os == "Windows":
                if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json'):
                    with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json', "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                else:
                    printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")
            elif main_os == "Darwin":
                if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json'):
                    with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json', "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                else:
                    printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")

        with open("FastFlagConfiguration.json", "w") as f:
            json.dump(fastFlagConfig, f, indent=4)

        printSuccessMessage("Successfully saved Bootstrap Settings!")

    def handleOption5():
        printWarnMessage("--- Sync to Fast Flag Configuration ---")
        global fastFlagConfig
        printMainMessage("Validating Bootstrap Install Directory..")
        if (fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir") and os.path.exists(fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir"))):
            if main_os == "Windows":
                if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json'):
                    with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json', "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                    printSuccessMessage("Successfully synced Bootstrap Settings!")
                else:
                    printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")
            elif main_os == "Darwin":
                if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json'):
                    with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json', "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                    printSuccessMessage("Successfully synced Bootstrap Settings!")
                else:
                    printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")
        else:
            printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")

    def handleOption6():
        printWarnMessage("--- Sync from Fast Flag Configuration ---")
        global fastFlagConfig
        printMainMessage("Validating Bootstrap Install Directory..")
        if (fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir") and os.path.exists(fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir"))):
            if main_os == "Windows":
                if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json'):
                    with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json', "r") as f:
                        fromFastFlagConfig = json.loads(f.read())
                    fromFastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"]
                    with open(f'FastFlagConfiguration.json', "w") as f:
                        json.dump(fromFastFlagConfig, f, indent=4)
                    printSuccessMessage("Successfully synced Bootstrap Settings!")
                else:
                    printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")
            elif main_os == "Darwin":
                if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json'):
                    with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json', "r") as f:
                        fromFastFlagConfig = json.loads(f.read())
                    fromFastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"]
                    with open(f'FastFlagConfiguration.json', "w") as f:
                        json.dump(fromFastFlagConfig, f, indent=4)
                    printSuccessMessage("Successfully synced Bootstrap Settings!")
                else:
                    printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")
        else:
            printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")

    def handleOption7():
        printWarnMessage("--- Credits ---")
        printMainMessage("1. Main Coding by \033[38;5;202m@EfazDev\033[0m")
        printMainMessage("2. Old Death Sound and Cursors were sourced from \033[38;5;165mBloxstrap files (https://github.com/pizzaboxer/bloxstrap)\033[0m")
        printMainMessage("3. AvatarEditorMaps were from \033[38;5;197mMielesgames's Map Files (https://github.com/Mielesgames/RobloxAvatarEditorMaps)\033[0m slightly edited to be usable for the current version of Roblox (as of the time of writing this)")
        printMainMessage("4. Some files were exported from the main macOS Roblox.app files. \033[38;5;202m(Logo was made using the Apple Pages icon, hued and then added the Roblox Logo)\033[0m")
        printMainMessage(f"5. macOS App was built using \033[38;5;39mpyinstaller\033[0m. You can recreate and deploy using this command (macOS only): \033[38;5;39mpyinstaller EfazRobloxBootstrap.spec --distpath Apps --noconfirm && zip -r -y ./Apps/EfazRobloxBootstrapMac.zip ./Apps/EfazRobloxBootstrap.app ./Apps/EfazRobloxBootstrapLoad.app && rm -rf ./build/ ./Apps/EfazRobloxBootstrapLoad/ && python3 Install.py --install\033[0m")
        if False:
            printMainMessage(f"Intel: \033[38;5;39mpyinstaller EfazRobloxBootstrap_MacIntel.spec --distpath Apps --noconfirm && zip -r -y ./Apps/EfazRobloxBootstrapMacIntel.zip ./Apps/EfazRobloxBootstrap.app ./Apps/EfazRobloxBootstrapLoad.app && rm -rf ./build/ ./Apps/EfazRobloxBootstrapLoad/ && {sys.executable} Install.py --install\033[0m")
        printMainMessage(f"6. Windows App was also built using \033[38;5;39mpyinstaller\033[0m. You can recreate and deploy using this command (windows only): \033[38;5;39mpyinstaller EfazRobloxBootstrap_Windows.spec --distpath Apps --noconfirm && rmdir /s /q build && del /q Apps\\EfazRobloxBootstrap\\* && {sys.executable} Install.py --install\033[0m")
        printDebugMessage(f"Operating System: {main_os}")
        printDebugMessage(f"Debug Mode Enabled")

    def handleOption8():
        printWarnMessage("--- End All Roblox Instances ---")
        printMainMessage("Are you sure you want to end all currently open Roblox instances?")
        a = input("> ")
        if isYes(a) == True:
            handler.endRoblox()

    def handleOption9():
        printWarnMessage("--- Reinstall Roblox ---")
        printMainMessage("Are you sure you want to reinstall Roblox?")
        a = input("> ")
        if isYes(a) == True:
            handler.installRoblox()

    def handleOption10(li=None):
        printWarnMessage("--- Roblox Link Shortcuts ---")
        if type(li) is str:
            if '://' in li:
                path = li.split('://', 1)[1]
            else:
                path = li.split(':', 1)[1]
            generated_shortcut_id = path.replace("shortcuts/", "")
            if type(fastFlagConfig.get("EFlagRobloxLinkShortcuts")) is dict:
                if fastFlagConfig["EFlagRobloxLinkShortcuts"].get(generated_shortcut_id):
                    shortcut_info = fastFlagConfig["EFlagRobloxLinkShortcuts"].get(generated_shortcut_id)
                    if type(shortcut_info.get("url")) is str and (shortcut_info.get("url").startswith("roblox:") or shortcut_info.get("url").startswith("roblox-player:")):
                        printSuccessMessage(f'Starting shortcut "{shortcut_info.get('name')}"!')
                        if len(given_args) > 1:
                            given_args[1] = shortcut_info["url"]
                        else:
                            given_args.append(shortcut_info["url"])
                    else:
                        printErrorMessage(f'You were redirected to a link shortcut with id "{generated_shortcut_id}" but it doesn\' have a valid url.')
                        input("> ")
                        exit()
                else:
                    printErrorMessage(f'You were redirected to a link shortcut with id "{generated_shortcut_id}" but it doesn\' exist under your settings.')
                    input("> ")
                    exit()
            else:
                printErrorMessage(f'You were redirected to a link shortcut with id "{generated_shortcut_id}" but it doesn\' exist under your settings.')
                input("> ")
                exit()
        else:
            generated_ui_options = []
            main_ui_options = {}
            if type(fastFlagConfig.get("EFlagRobloxLinkShortcuts")) is dict:
                for i, v in fastFlagConfig.get("EFlagRobloxLinkShortcuts").items():
                    if v and v.get("name") and v.get("id") and v.get("url"):
                        generated_ui_options.append({"index": 1, "message": f"{v.get('name')} [{i}]", "shortcut_info": v})
            generated_ui_options.append({"index": 999999, "message": "Create a new shortcut"})
            generated_ui_options.append({"index": 1000000, "message": "Delete a shortcut"})
            count = 1
            for i in generated_ui_options:
                printMainMessage(f"[{str(count)}] = {i['message']}")
                main_ui_options[str(count)] = i
                count += 1
            res = input("> ")
            if main_ui_options.get(res):
                opt = main_ui_options[res]
                if opt["index"] == 999999:
                    def loo():
                        printMainMessage("Enter the name to use for the shortcut: ")
                        name = input("> ")
                        printMainMessage("Enter the url to use for the shortcut (starts with \"roblox:\" or \"roblox-player:\"): ")
                        printMainMessage("Use this guide to help create it: https://github.com/pizzaboxer/bloxstrap/wiki/A-deep-dive-on-how-the-Roblox-bootstrapper-works#starting-roblox")
                        def urll():
                            ura = input("> ")
                            if ura.startswith("roblox:") or ura.startswith("roblox-player:"):
                                return ura
                            else:
                                printErrorMessage("This is not a valid Roblox URL Scheme. Please try again!")
                                return urll()
                        ur = urll()
                        printMainMessage("Enter the key to be defined for this shortcut, this will be used for a url scheme: ")
                        key = input("> ") 
                        printMainMessage("Confirm the shortcut below? (y/n)")
                        printMainMessage(f"Name: {name}")
                        printMainMessage(f"URL: {ur}")
                        printMainMessage(f"Key: {key}")
                        if isYes(input("> ")) == True:
                            if fastFlagConfig.get("EFlagRobloxLinkShortcuts"):
                                fastFlagConfig.get("EFlagRobloxLinkShortcuts")[key] = {"url": ur, "name": name, "id": key}
                            else:
                                fastFlagConfig["EFlagRobloxLinkShortcuts"] = {}
                                fastFlagConfig["EFlagRobloxLinkShortcuts"][key] = {"url": ur, "name": name, "id": key}
                        if (fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir") and os.path.exists(fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir"))):
                            if main_os == "Windows":
                                if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json'):
                                    with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json', "w") as f:
                                        json.dump(fastFlagConfig, f, indent=4)
                                else:
                                    printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")
                            elif main_os == "Darwin":
                                if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json'):
                                    with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json', "w") as f:
                                        json.dump(fastFlagConfig, f, indent=4)
                                else:
                                    printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")

                        with open("FastFlagConfiguration.json", "w") as f:
                            json.dump(fastFlagConfig, f, indent=4)
                        printMainMessage("Would you like to create an another shortcut? (y/n)")
                        if isYes(input("> ")) == True:
                            loo()
                    loo()
                    handleOptionSelect(mes="Link Creation has finished! Would you like to continue to Roblox?")
                elif opt["index"] == 1000000:
                    if type(fastFlagConfig.get("EFlagRobloxLinkShortcuts")) is dict:
                        def loo():
                            if type(fastFlagConfig.get("EFlagRobloxLinkShortcuts")) is dict:
                                printMainMessage("Enter the key of the shortcut to delete: ")
                                key = input("> ")
                                if fastFlagConfig.get("EFlagRobloxLinkShortcuts").get(key):
                                    info = fastFlagConfig.get("EFlagRobloxLinkShortcuts")
                                    printMainMessage("Confirm the shortcut below? (y/n)")
                                    printMainMessage(f"Name: {info['name']}")
                                    printMainMessage(f"URL: {info['url']}")
                                    printMainMessage(f"Key: {key}")
                                    if isYes(input("> ")) == True:
                                        fastFlagConfig["EFlagRobloxLinkShortcuts"][key] = {}
                                    if (fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir") and os.path.exists(fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir"))):
                                        if main_os == "Windows":
                                            if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json'):
                                                with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}\\FastFlagConfiguration.json', "w") as f:
                                                    json.dump(fastFlagConfig, f, indent=4)
                                            else:
                                                printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")
                                        elif main_os == "Darwin":
                                            if os.path.exists(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json'):
                                                with open(f'{fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir")}/FastFlagConfiguration.json', "w") as f:
                                                    json.dump(fastFlagConfig, f, indent=4)
                                            else:
                                                printErrorMessage("Bootstrap Sync is not supported since the original unextracted directory is not found.")

                                    with open("FastFlagConfiguration.json", "w") as f:
                                        json.dump(fastFlagConfig, f, indent=4)
                                    printMainMessage("Would you like to delete an another shortcut? (y/n)")
                                    if isYes(input("> ")) == True:
                                        loo()
                                else:
                                    printErrorMessage("Key doesn't exist! Let's try again!")
                                    loo()
                        loo()
                        handleOptionSelect(mes="Link Deletion has finished! Would you like to continue to Roblox?")
                    else:
                        printErrorMessage("You have no shortcuts created!")
                        handleOptionSelect(mes="Link Deletion has finished! Would you like to continue to Roblox?")
                else:
                    if type(opt["shortcut_info"]["url"]) is str and (opt["shortcut_info"].startswith("roblox:") or opt["shortcut_info"].startswith("roblox-player:")):
                        printSuccessMessage(f"Starting shortcut \"{opt['shortcut_info']['name']}\"!")
                        if len(given_args) > 1:
                            given_args[1] = opt["shortcut_info"]["url"]
                        else:
                            given_args.append(opt["shortcut_info"]["url"])
                    else:
                        exit()
            else:
                exit()
    def handleOptionSelect(mes="Option finished! Would you like to continue to Roblox? (y/n)"):
        printWarnMessage(mes)
        a = input("> ")
        if isYes(a) == False:
            exit()

    def displayNotification(title, message):
        if main_os == "Darwin":
            if os.path.exists("/Applications/EfazRobloxBootstrap.app/Contents/Resources/"):
                with open("/Applications/EfazRobloxBootstrap.app/Contents/Resources/MacOSNotification", "w") as f:
                    json.dump({"title": title, "message": message}, f)
        elif main_os == "Windows":
            try:
                from plyer import notification
            except Exception as e:
                pip().install(["plyer"])
                from plyer import notification
            notification.notify(
                title = title,
                message = message,
                app_icon = "AppIcon.ico",
                timeout = 30,
            )

    continue_to_url_handler = False
    if len(given_args) > 1:
        if "efaz-bootstrap:" in given_args[1]:
            continue_to_url_handler = True

    if (not (fastFlagConfig.get("EFlagRemoveMenuAndSkipToRoblox") == True)) or continue_to_url_handler == True:
        if (len(given_args) < 2):
            if not (fastFlagConfig.get("EFlagCompletedTutorial") == True):
                printWarnMessage("--- Tutorial ---")
                printMainMessage("Welcome to Efaz's Roblox Bootstrap!")
                printMainMessage("Efaz's Roblox Bootstrap is a Roblox bootstrap that allows you to apply modifications to your Roblox Client using Fast Flags or Files automatically!")
                if main_os == "Darwin":
                    if os.path.exists("/Applications/EfazRobloxBootstrap.app"):
                        printMainMessage("It seems like everything seems to be working and now you have reached the next part!")
                    else:
                        printMainMessage("I'm sorry, but you're not quite finished yet. Please run Install.py instead of Main.py!!")
                        input("> ")
                        exit()
                elif main_os == "Windows":
                    if os.path.exists(f"{os.getenv('LOCALAPPDATA')}\\EfazRobloxBootstrap\\"):
                        printMainMessage("It seems like everything seems to be working and now you have reached the next part!")
                    else:
                        printMainMessage("I'm sorry, but you're not quite finished yet. Please run Install.py instead of Main.py!!")
                        input("> ")
                        exit()

                printMainMessage("Before we get started, we're showing you some information for you to know.")
                printWarnMessage("--- Information 1 ---")
                if main_os == "Darwin":
                    printMainMessage("First, you may need to know that after you go to Roblox through this bootstrap, Roblox will not be able to be opened normally.")
                    printMainMessage("This is because of macOS trying to scan signatures but failing.")
                    printMainMessage("If you want to uninstall this bootstrap, you may run Uninstall.py which is located in the same folder as the Install.py you ran to be here! However, you can use the Reinstall Roblox option in the bootstrap menu to prevent uninstalling this.")
                    printMainMessage("Don't worry though, you will be able to join through your web browser since the app will sync.")
                else:
                    printMainMessage("You're not on macOS, so you can skip this info.")
                input("> ")
                printWarnMessage("--- Information 2 ---")
                printMainMessage("Second, some features are based on Activity Tracking on your Roblox Client.")
                printMainMessage("This app will use your Roblox logs to track data such as Game Join Data, Discord Presences, BloxstrapRPC and more!")
                printMainMessage("Don't worry, your Roblox account is safely secured and this won't get you banned.")
                input("> ")
                printWarnMessage("--- Information 3 ---")
                displayNotification("Hello!", "If you see this, your notifications are set up! Great job!")
                printMainMessage("We just sent a notification to your device so that you can enable Notifications or not.")
                printMainMessage("Depending on your OS (Windows or macOS), you may be able to select Allow for features like Server Locations to work!")
                input("> ")
                printWarnMessage("--- Step 1 ---")
                printMainMessage("Alright, now to the actual stuff, firstly, it's important you best understand on how the choosing works.")
                printMainMessage('Let\'s start off with a quick input! Let\'s say you want to enable this option (use the prompt here for the example), enter "y" or "yes"!')
                def a():
                    b = input("> ")
                    if isYes(b) == True:
                        return
                    else:
                        printErrorMessage("Uhm, not quite, try again!")
                        a()
                a()
                printWarnMessage("--- Step 2 ---")
                printMainMessage("Congrats! You completed the first step!")
                printMainMessage('Now, let\'s try that again! But instead, enter "n" or "no" for you don\'t want this feature!')
                def a():
                    b = input("> ")
                    if isNo(b) == True:
                        return
                    else:
                        printErrorMessage("Uhm, not quite, try again!")
                        a()
                a()
                printWarnMessage("--- Step 3 ---")
                printMainMessage("You're getting good at this!")
                printMainMessage('Now, let\'s learn about how you select from a list. Take the list below for an example.')
                printMainMessage("Try selecting a number that is next to that option!")
                generated_ui_options = []
                main_ui_options = {}
                generated_ui_options.append({"index": 1, "message": "Do jumping-jacks", "func": handleOption1})
                generated_ui_options.append({"index": 2, "message": "Do push-ups", "func": handleOption1})
                generated_ui_options.append({"index": 3, "message": "Do curl-ups", "func": handleOption1})
                generated_ui_options.append({"index": 4, "message": "Do neither", "func": handleOption1})
                printWarnMessage("--- Select Option ---")
                count = 1
                for i in generated_ui_options:
                    printMainMessage(f"[{str(count)}] = {i['message']}")
                    main_ui_options[str(count)] = i
                    count += 1
                def a():
                    res = input("> ")
                    if main_ui_options.get(res):
                        opt = main_ui_options[res]
                        printSuccessMessage(f"You have selected {opt.get('message')}!")
                    else:
                        printErrorMessage("Uhm, not quite, try again!")
                        return a()
                a()
                printWarnMessage("--- Step 4 ---")
                printMainMessage("Nice job! Oh yea, for this time, it will repeat with a Not quite, but after this, it will close the window.")
                printMainMessage("However, if you do meet with an option with a *, this means that any input will result with that option.")
                printMainMessage("Anyways, welcome to step 4! Here, you can select your settings!")
                printMainMessage("(In the settings area, you can just input nothing or anything else instead of y or n to skip the option without affecting the current state of it.)")
                printMainMessage("See you after a little bit!")
                input("> ")
                handleOption4()
                printWarnMessage("--- Step 5 ---")
                printMainMessage("Welcome back! I hope you have enabled some stuffs you may want!")
                printMainMessage("Now, let's get more customizable! Next, you will be able to select your fast flags.")
                printMainMessage("But before, prepare yourself your Roblox User ID. It will be used for some settings depending on what you select.")
                input("> ")
                handleOption3()
                printWarnMessage("--- Final Touches ---")
                printMainMessage("Woo hoo! You finally reached the end of this tutorial!")
                printMainMessage("I hope you learned from this and how you may use Roblox using this bootstrap!")
                printMainMessage("For now, before I exit, I hope you have a great day and welcome to your new Roblox app!")
                printMainMessage("[You will return to the main menu!]")
                with open("FastFlagConfiguration.json", "r") as f:
                    try:
                        fastFlagConfig = json.loads(f.read())
                    except Exception as e:
                        loadedJSON = False
                fastFlagConfig["EFlagCompletedTutorial"] = True
                with open("FastFlagConfiguration.json", "w") as f:
                    json.dump(fastFlagConfig, f, indent=4)
                input("> ")
            if not (fastFlagConfig.get("EFlagSkipEfazRobloxBootstrapPromptUI") == True):
                generated_ui_options = []
                main_ui_options = {}
                generated_ui_options.append({"index": 1, "message": "Continue to Roblox", "func": handleOption1, "include_go_to_roblox": False})
                generated_ui_options.append({"index": 3, "message": "Run Fast Flag Installer", "func": handleOption3, "include_go_to_roblox": True, "include_message": "Installer has finished! Would you like to go to Roblox? (y/n)"})
                generated_ui_options.append({"index": 4, "message": "Set Settings", "func": handleOption4, "include_go_to_roblox": True, "include_message": "Settings has been saved! Would you like to go to Roblox? (y/n)"})
                generated_ui_options.append({"index": 5, "message": "Roblox Link Shortcuts", "func": handleOption10, "include_go_to_roblox": False, "include_message": "Roblox Start URL is set! Would you like to run it now? (y/n)"})
                generated_ui_options.append({"index": 6, "message": "End All Roblox Instances", "func": handleOption8, "include_go_to_roblox": True, "include_message": "Roblox Instances have been ended! Would you like to rerun it? (y/n)"})
                generated_ui_options.append({"index": 7, "message": "Reinstall Roblox", "func": handleOption9, "include_go_to_roblox": True, "include_message": "Roblox has been reinstalled! Would you like to run it now? (y/n)"})
                generated_ui_options.append({"index": 99, "message": "Credits", "func": handleOption7, "include_go_to_roblox": True, "include_message": "Would you like to go to Roblox? (y/n)"})
                if main_os == "Darwin":
                    if (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True):
                        generated_ui_options.append({"index": 2, "message": "Generate Another Roblox Instance", "func": handleOption2, "include_go_to_roblox": False})
                if (fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir") and os.path.exists(fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir"))):
                    generated_ui_options.append({"index": 10, "message": "Sync to Fast Flag Configuration", "func": handleOption5, "include_go_to_roblox": True, "include_message": "Sync finished! Would you like to run Roblox now? (y/n)"})
                    generated_ui_options.append({"index": 11, "message": "Sync from Fast Flag Configuration", "func": handleOption6, "include_go_to_roblox": True, "include_message": "Sync finished! Would you like to run Roblox now? (y/n)"})

                generated_ui_options = sorted(generated_ui_options, key=lambda x: x["index"])
                printWarnMessage("--- Select Mode ---")
                count = 1
                for i in generated_ui_options:
                    printMainMessage(f"[{str(count)}] = {i['message']}")
                    main_ui_options[str(count)] = i
                    count += 1

                res = input("> ")
                if main_ui_options.get(res):
                    opt = main_ui_options[res]
                    opt["func"]()
                    if opt.get("include_go_to_roblox") == True: handleOptionSelect(opt.get("include_message"))
                else:
                    exit()

                loadedJSON = True
                with open("FastFlagConfiguration.json", "r") as f:
                    try:
                        fastFlagConfig = json.loads(f.read())
                    except Exception as e:
                        loadedJSON = False

                if fastFlagConfig.get("EFlagSkipEfazRobloxBootstrapPromptUI") == None:
                    printMainMessage("Would you like to skip the Bootstrap Start UI in the future? (y/n)")
                    skipInFuture = input("> ")
                    
                    if isYes(skipInFuture) == True:
                        fastFlagConfig["EFlagSkipEfazRobloxBootstrapPromptUI"] = True
                    else:
                        fastFlagConfig["EFlagSkipEfazRobloxBootstrapPromptUI"] = False

                    with open("FastFlagConfiguration.json", "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
            else:
                printWarnMessage("--- Continue to Roblox? ---")
                printMainMessage("[1/*] = Continue")
                printMainMessage("[2] = Revert Remove UI")
                printMainMessage("[3] = End Process")
                res = input("> ")
                if res == "2":
                    fastFlagConfig["EFlagSkipEfazRobloxBootstrapPromptUI"] = False
                    with open("FastFlagConfiguration.json", "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                    printSuccessMessage("Reverted successfully!")
                    input("> ")
                    exit()
                elif res == "3":
                    exit()
        elif len(given_args) > 1:
            url = given_args[1]
            if "efaz-bootstrap" in url:
                if "continue" in url:
                    handleOption1()
                elif "new" in url:
                    handleOption2()
                elif "fflag-install" in url:
                    handleOption3()
                    handleOptionSelect()
                elif "settings" in url:
                    handleOption4()
                    handleOptionSelect()
                elif "sync-to-install" in url:
                    handleOption5()
                    handleOptionSelect()
                elif "sync-from-install" in url:
                    handleOption6()
                    handleOptionSelect()
                elif "end-roblox" in url:
                    handleOption8()
                    handleOptionSelect()
                elif "reinstall-roblox" in url:
                    handleOption9()
                    handleOptionSelect()
                elif ("credits" in url) or ("about" in url):
                    handleOption7()
                    handleOptionSelect()
                elif ("shortcuts/" in url):
                    handleOption10(url)
                else:
                    printDebugMessage(f"Unknown command: {url}")
                    printWarnMessage("--- Continue to Roblox? ---")
                    printMainMessage("[1] = Continue")
                    printMainMessage("[69] = Remove Skip UI")
                    printMainMessage("[*] = End Process")
                    res = input("> ")
                    if res == "1":
                        handleOption1()
                    elif res == "69":
                        fastFlagConfig["EFlagSkipEfazRobloxBootstrapPromptUI"] = False
                        with open("FastFlagConfiguration.json", "w") as f:
                            json.dump(fastFlagConfig, f, indent=4)
                        printSuccessMessage("Reverted successfully!")
                        printWarnMessage("Option finished! Would you like to continue to Roblox? (y/n)")
                        a = input("> ")
                        if isYes(a) == False:
                            exit()
                    else:
                        exit()
    if (not (fastFlagConfig.get("EFlagDisableBootstrapChecks") == True)) and os.path.exists("Version.json"):
        printWarnMessage("--- Checking for Bootstrap Updates ---")
        skip_check = False
        try:
            import requests
        except Exception as e:
            printMainMessage("Some modules are not installed. Do you want to install all the modules required now? (y/n)")
            pip().install(["requests"])
            import requests
            printSuccessMessage("Successfully installed modules!")
        if skip_check == False:
            latest_vers_res = requests.get("https://raw.githubusercontent.com/EfazDev/roblox-bootstrap/main/Version.json")
            if latest_vers_res.ok:
                latest_vers = latest_vers_res.json()
                if currentVersion.get("latest_version"):
                    if currentVersion.get("latest_version", "1.0.0") < latest_vers.get("latest_version", "1.0.0"):
                        printDebugMessage(f"Update v{latest_vers['latest_version']} detected!")
                        printWarnMessage("--- New Bootstrap Update ---")
                        printMainMessage(f"Would you like to install v{latest_vers['latest_version']}?")
                        printMainMessage(f"v{currentVersion.get('version', '1.0.0')} => v{latest_vers['latest_version']}")
                        if isYes(input("> ")) == True:
                            printMainMessage("Downloading latest version..")
                            subprocess.run(["curl", "-L", "https://github.com/EfazDev/roblox-bootstrap/archive/refs/heads/main.zip", "-o", "./Update.zip"], check=True)
                            printMainMessage("Downloaded! Extracting ZIP now!")
                            if main_os == "Darwin":
                                subprocess.run(["unzip", "-o", "Update.zip", "-d", "./Update/"], check=True)
                                printMainMessage("Extracted successfully! Filtering out files for update!")
                                for file in os.listdir("./Update/roblox-bootstrap-main/"):
                                    src_path = os.path.join("./Update/roblox-bootstrap-main/", file)
                                    dest_path = os.path.join("./", file)
                                    
                                    if os.path.isdir(src_path):
                                        shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
                                    else:
                                        if not file.endswith(".json"):
                                            shutil.copy2(src_path, dest_path)
                            elif main_os == "Windows":
                                subprocess.run(["powershell", "-command", f"Expand-Archive -Path 'Update.zip' -DestinationPath './Update/' -Force"], check=True)
                                printMainMessage("Extracted successfully! Filtering out files for update!")
                                for file in os.listdir("./Update/roblox-bootstrap-main/"):
                                    src_path = os.path.join("./Update/roblox-bootstrap-main/", file)
                                    dest_path = os.path.join("./", file)
                                    
                                    if os.path.isdir(src_path):
                                        shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
                                    else:
                                        if not file.endswith(".json"):
                                            shutil.copy2(src_path, dest_path)
                            printMainMessage("Cleaning up files..")
                            os.remove("Update.zip")
                            shutil.rmtree("./Update/")
                            if latest_vers.get("versions_required_install"):
                                if latest_vers.get("versions_required_install").get(currentVersion.get('version', '1.0.0')) == True:
                                    subprocess.run(args=[sys.executable, "Install.py", "--install"])
                            printSuccessMessage(f"Update to v{latest_vers['version']} was finished successfully! Please restart this script!")
                            input("> ")
                            exit()
                        else:
                            printDebugMessage("User rejected update.")
                    else:
                        printMainMessage("Running latest version of Bootstrap!")
                else:
                    printDebugMessage("There was an error reading the latest version.")
            else:
                printDebugMessage("Update Check Response failed.")
    if (not (fastFlagConfig.get("EFlagDisableRobloxUpdateChecks") == True)):
        printWarnMessage("--- Checking for Roblox Updates ---")
        latest_version = handler.getLatestClientVersion(debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
        current_version = handler.getCurrentClientVersion()

        if fastFlagConfig.get("EFlagFreshCopyRoblox") == True:
            printWarnMessage("--- Installing Latest Roblox Version ---")
            handler.installRoblox(debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
            time.sleep(3)
        elif latest_version["success"] == True and current_version["success"] == True:
            if current_version["isClientVersion"] == True:
                if current_version["version"] == latest_version["client_version"]:
                    printMainMessage("Running current version of Roblox!")
                else:
                    printWarnMessage("--- Installing Latest Roblox Version ---")
                    handler.installRoblox(debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
                    time.sleep(3)
            else:
                if current_version["version"] == latest_version["short_version"]:
                    printMainMessage("Running latest version of Roblox!")
                else:
                    printWarnMessage("--- Installing Latest Roblox Version ---")
                    handler.installRoblox(debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
                    time.sleep(3)
        else:
            printErrorMessage("There was issue while checking for updates.")

    if main_os == "Windows":
        if os.path.exists(os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap", "EfazRobloxBootstrap.exe")):
            if not (fastFlagConfig.get("EFlagDisableURLSchemeInstall") == True):
                printWarnMessage("--- Configuring Windows Registry ---")
                bootstrap_folder_path = os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap")
                bootstrap_path = os.path.join(bootstrap_folder_path, "EfazRobloxBootstrap.exe")
                try:
                    import requests
                    import winreg
                    import win32com.client
                except Exception as e:
                    pip().install(["requests"])
                    pip().install(["pywin32"])
                    import requests
                    import winreg
                    import win32com.client
                printMainMessage("Setting up URL Schemes..")
                def set_url_scheme(protocol, exe_path):
                    protocol_key = r"Software\Classes\{}".format("")
                    command_key = r"Software\Classes\{}\shell\open\command".format(protocol)

                    try:
                        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, protocol_key) as key:
                            winreg.SetValue(key, "", winreg.REG_SZ, "URL:{}".format(protocol))
                            winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, "")
                        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, command_key) as key:
                            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, '"{}" "%1"'.format(exe_path))
                        printSuccessMessage(f"URL scheme '{protocol}' has been set for '{exe_path}'")
                    except Exception as e:
                        printErrorMessage(f"An error occurred: {e}")
                set_url_scheme("efaz-bootstrap", bootstrap_path)
                set_url_scheme("roblox-player", bootstrap_path)
                set_url_scheme("roblox", bootstrap_path)

            printMainMessage("Setting up shortcuts..")
            def create_shortcut(target_path, shortcut_path, working_directory=None, icon_path=None):
                shell = win32com.client.Dispatch('WScript.Shell')
                shortcut = shell.CreateShortcut(shortcut_path)
                shortcut.TargetPath = target_path
                if working_directory: shortcut.WorkingDirectory = working_directory
                if icon_path: shortcut.IconLocation = icon_path
                shortcut.save()
            create_shortcut(bootstrap_path, os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'), 'EfazRobloxBootstrap.lnk'))
            create_shortcut(bootstrap_path, os.path.join(os.path.join(os.path.join(os.environ['APPDATA']), 'Microsoft', 'Windows', 'Start Menu', 'Programs'), 'EfazRobloxBootstrap.lnk'))

            printMainMessage("Calling Windows to mark program as installed.")
            app_key = "Software\\EfazRobloxBootstrap"
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, app_key) as key:
                winreg.SetValueEx(key, "InstallPath", 0, winreg.REG_SZ, bootstrap_folder_path)
                winreg.SetValueEx(key, "Installed", 0, winreg.REG_DWORD, 1)

            registry_path = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\EfazRobloxBootstrap"
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, registry_path) as key:
                winreg.SetValueEx(key, "UninstallString", 0, winreg.REG_SZ, f"py {os.path.join(bootstrap_folder_path, "Uninstall.py")}")
                winreg.SetValueEx(key, "DisplayName", 0, winreg.REG_SZ, "Efaz's Roblox Bootstrap")
                winreg.SetValueEx(key, "DisplayVersion", 0, winreg.REG_SZ, currentVersion["version"])
                winreg.SetValueEx(key, "DisplayIcon", 0, winreg.REG_SZ, os.path.join(bootstrap_folder_path, "AppIcon.ico"))

    printWarnMessage("--- Preparing Roblox ---")
    def prepareRoblox():
        if handler.getIfRobloxIsOpen():
            if main_os == "Windows":
                if os.path.exists(os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap", "EfazRobloxBootstrap.exe")):
                    handler.endRoblox()
                    time.sleep(2)

        global fastFlagConfig
        if fastFlagConfig.get("EFlagRemoveBuilderFont") == True or (fastFlagConfig.get("EFlagEnableNewFontNameMappingABTest2") and fastFlagConfig.get("EFlagEnableNewFontNameMappingABTest2").lower() == "false"):
            printMainMessage("Changing Font Files..")
            copyFile(f"{stored_font_folder_destinations[found_platform]}GothamSSm-Black.otf", f"{stored_font_folder_destinations[found_platform]}BuilderSans-ExtraBold.otf")
            copyFile(f"{stored_font_folder_destinations[found_platform]}GothamSSm-Medium.otf", f"{stored_font_folder_destinations[found_platform]}BuilderSans-Bold.otf")
            copyFile(f"{stored_font_folder_destinations[found_platform]}GothamSSm-Medium.otf", f"{stored_font_folder_destinations[found_platform]}BuilderSans-Medium.otf")
            copyFile(f"{stored_font_folder_destinations[found_platform]}GothamSSm-Book.otf", f"{stored_font_folder_destinations[found_platform]}BuilderSans-Regular.otf")
            copyFile(f"{stored_font_folder_destinations[found_platform]}GothamSSm-Black.otf", f"{stored_font_folder_destinations[found_platform]}Montserrat-Black.ttf")
            copyFile(f"{stored_font_folder_destinations[found_platform]}GothamSSm-Bold.otf", f"{stored_font_folder_destinations[found_platform]}Montserrat-Bold.ttf")
            copyFile(f"{stored_font_folder_destinations[found_platform]}GothamSSm-Medium.otf", f"{stored_font_folder_destinations[found_platform]}Montserrat-Medium.ttf")
            copyFile(f"{stored_font_folder_destinations[found_platform]}GothamSSm-Book.otf", f"{stored_font_folder_destinations[found_platform]}Montserrat-Regular.ttf")
            printSuccessMessage("Successfully changed Builder San files to GothamSSm!")
        
        if fastFlagConfig.get("EFlagEnableModModes") == True:
            if fastFlagConfig.get("EFlagSelectedModMode") and os.path.exists(os.path.join(os.path.curdir, "ModModes", fastFlagConfig.get("EFlagSelectedModMode"))):
                printMainMessage("Applying Mods..")
                if main_os == "Windows":
                    shutil.copytree(f"{os.path.curdir}\\ModModes\\{fastFlagConfig['EFlagSelectedModMode']}\\", f"{stored_content_folder_destinations[found_platform]}\\", dirs_exist_ok=True)
                elif main_os == "Darwin":
                    shutil.copytree(f"{os.path.curdir}/ModModes/{fastFlagConfig['EFlagSelectedModMode']}/", f"{stored_content_folder_destinations[found_platform]}/", dirs_exist_ok=True)
                printSuccessMessage("Successfully changed unmodded files to mod mode!")
            else:
                printMainMessage("Applying Mods..")
                if main_os == "Windows":
                    shutil.copytree(f"{os.path.curdir}\\ModModes\\Original\\", f"{stored_content_folder_destinations[found_platform]}\\", dirs_exist_ok=True)
                elif main_os == "Darwin":
                    shutil.copytree(f"{os.path.curdir}/ModModes/Original/", f"{stored_content_folder_destinations[found_platform]}/", dirs_exist_ok=True)
                printSuccessMessage("Successfully changed modded files to original!")
        else:
            printMainMessage("Applying Mods..")
            if main_os == "Windows":
                shutil.copytree(f"{os.path.curdir}\\ModModes\\Original\\", f"{stored_content_folder_destinations[found_platform]}\\", dirs_exist_ok=True)
            elif main_os == "Darwin":
                shutil.copytree(f"{os.path.curdir}/ModModes/Original/", f"{stored_content_folder_destinations[found_platform]}/", dirs_exist_ok=True)
            printSuccessMessage("Successfully changed modded files to original!")

        if fastFlagConfig.get("EFlagEnableChangeAvatarEditorBackground") == True:
            printMainMessage("Changing Current Avatar Editor to Set Avatar Background..")
            if main_os == "Windows":
                copyFile(f"{os.path.curdir}\\AvatarEditorMaps\\{fastFlagConfig['EFlagAvatarEditorBackground']}\\AvatarBackground.rbxl", f"{stored_content_folder_destinations[found_platform]}ExtraContent\\places\\Mobile.rbxl")
            elif main_os == "Darwin":
                copyFile(f"{os.path.curdir}/AvatarEditorMaps/{fastFlagConfig['EFlagAvatarEditorBackground']}/AvatarBackground.rbxl", f"{stored_content_folder_destinations[found_platform]}ExtraContent/places/Mobile.rbxl")
            printSuccessMessage("Successfully changed current avatar editor with a set background!")
        else:
            printMainMessage("Changing Current Avatar Editor to Original Avatar Background..")
            if main_os == "Windows":
                copyFile(f"{os.path.curdir}\\AvatarEditorMaps\\Original\\AvatarBackground.rbxl", f"{stored_content_folder_destinations[found_platform]}ExtraContent\\places\\Mobile.rbxl")
            elif main_os == "Darwin":
                copyFile(f"{os.path.curdir}/AvatarEditorMaps/Original/AvatarBackground.rbxl", f"{stored_content_folder_destinations[found_platform]}ExtraContent/places/Mobile.rbxl")
            printSuccessMessage("Successfully changed current avatar editor to original background!")

        if fastFlagConfig.get("EFlagEnableChangeCursor") == True:
            printMainMessage("Changing Current Cursor to Set Cursor..")
            if main_os == "Windows":
                copyFile(f"{os.path.curdir}\\Cursors\\{fastFlagConfig['EFlagSelectedCursor']}\\ArrowCursor.png", f"{stored_content_folder_destinations[found_platform]}content\\textures\\Cursors\\KeyboardMouse\\ArrowCursor.png")
                copyFile(f"{os.path.curdir}\\Cursors\\{fastFlagConfig['EFlagSelectedCursor']}\\ArrowFarCursor.png", f"{stored_content_folder_destinations[found_platform]}content\\textures\\Cursors\\KeyboardMouse\\ArrowFarCursor.png")
            elif main_os == "Darwin":
                copyFile(f"{os.path.curdir}/Cursors/{fastFlagConfig['EFlagSelectedCursor']}/ArrowCursor.png", f"{stored_content_folder_destinations[found_platform]}content/textures/Cursors/KeyboardMouse/ArrowCursor.png")
                copyFile(f"{os.path.curdir}/Cursors/{fastFlagConfig['EFlagSelectedCursor']}/ArrowFarCursor.png", f"{stored_content_folder_destinations[found_platform]}content/textures/Cursors/KeyboardMouse/ArrowFarCursor.png")
            printSuccessMessage("Successfully changed current cursor with a set cursor image!")
        else:
            printMainMessage("Changing Current Cursor to Original Cursor..")
            if main_os == "Windows":
                copyFile(f"{os.path.curdir}\\Cursors\\Original\\ArrowCursor.png", f"{stored_content_folder_destinations[found_platform]}content\\textures\\Cursors\\KeyboardMouse\\ArrowCursor.png")
                copyFile(f"{os.path.curdir}\\Cursors\\Original\\ArrowFarCursor.png", f"{stored_content_folder_destinations[found_platform]}content\\textures\\Cursors\\KeyboardMouse\\ArrowFarCursor.png")
            elif main_os == "Darwin":
                copyFile(f"{os.path.curdir}/Cursors/Original/ArrowCursor.png", f"{stored_content_folder_destinations[found_platform]}content/textures/Cursors/KeyboardMouse/ArrowCursor.png")
                copyFile(f"{os.path.curdir}/Cursors/Original/ArrowFarCursor.png", f"{stored_content_folder_destinations[found_platform]}content/textures/Cursors/KeyboardMouse/ArrowFarCursor.png")
            printSuccessMessage("Successfully changed current cursor with original cursor image!")

        if fastFlagConfig.get("EFlagEnableChangeDeathSound") == True:
            printMainMessage("Changing Current Death Sound to Set Sound File..")
            if main_os == "Windows":
                copyFile(f"{os.path.curdir}\\DeathSounds\\{fastFlagConfig['EFlagSelectedDeathSound']}", f"{stored_content_folder_destinations[found_platform]}content\\sounds\\ouch.ogg")
            elif main_os == "Darwin":
                copyFile(f"{os.path.curdir}/DeathSounds/{fastFlagConfig['EFlagSelectedDeathSound']}", f"{stored_content_folder_destinations[found_platform]}content/sounds/ouch.ogg")
            printSuccessMessage("Successfully changed current death sound with a set sound file!")
        else:
            printMainMessage("Changing Current Death Sound to Original Sound File..")
            if main_os == "Windows":
                copyFile(f"{os.path.curdir}\\DeathSounds\\New.ogg", f"{stored_content_folder_destinations[found_platform]}content\\sounds\\ouch.ogg")
            elif main_os == "Darwin":
                copyFile(f"{os.path.curdir}/DeathSounds/New.ogg", f"{stored_content_folder_destinations[found_platform]}content/sounds/ouch.ogg")
            printSuccessMessage("Successfully changed current death sound with original sound file!")

        if fastFlagConfig.get("EFlagEnableChangeBrandIcons") == True:
            if main_os == "Darwin":
                printMainMessage("Changing Current App Icon..")
                copyFile(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/AppIcon.icns", f"{stored_content_folder_destinations[found_platform]}AppIcon.icns")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/MenuIcon.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/MenuIcon.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/TopBar/coloredlogo.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/MenuIcon@2x.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/MenuIcon@2x.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/TopBar/coloredlogo@2x.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/MenuIcon@3x.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/MenuIcon@3x.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/TopBar/coloredlogo@3x.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxLogo.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxLogo.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/ScreenshotHud/RobloxLogo.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxLogo@2x.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxLogo@2x.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/ScreenshotHud/RobloxLogo@2x.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxLogo@3x.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxLogo@3x.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/ScreenshotHud/RobloxLogo@3x.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxNameIcon.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxNameIcon.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/RobloxNameIcon.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxTilt.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxTilt.png", f"{stored_content_folder_destinations[found_platform]}content/textures/loading/robloxTilt.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxTilt.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/{fastFlagConfig['EFlagSelectedBrandLogo']}/RobloxTilt.png", f"{stored_content_folder_destinations[found_platform]}content/textures/loading/robloxTiltRed.png")
                printSuccessMessage("Successfully changed current app icon! It may take a moment for macOS to identify it!")
            else:
                printDebugMessage("Change App Icon while on an another operating system..?")
        else:
            if main_os == "Darwin":
                printMainMessage("Changing Current App Icon..")
                copyFile(f"{os.path.curdir}/RobloxBrand/Original/AppIcon.icns", f"{stored_content_folder_destinations[found_platform]}AppIcon.icns")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/Original/MenuIcon.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/Original/MenuIcon.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/TopBar/coloredlogo.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/Original/MenuIcon@2x.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/Original/MenuIcon@2x.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/TopBar/coloredlogo@2x.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/Original/MenuIcon@3x.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/Original/MenuIcon@3x.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/TopBar/coloredlogo@3x.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/Original/RobloxLogo.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/Original/RobloxLogo.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/ScreenshotHud/RobloxLogo.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/Original/RobloxLogo@2x.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/Original/RobloxLogo@2x.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/ScreenshotHud/RobloxLogo@2x.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/Original/RobloxLogo@3x.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/Original/RobloxLogo@3x.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/ScreenshotHud/RobloxLogo@3x.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/Original/RobloxNameIcon.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/Original/RobloxNameIcon.png", f"{stored_content_folder_destinations[found_platform]}content/textures/ui/RobloxNameIcon.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/Original/RobloxTilt.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/Original/RobloxTilt.png", f"{stored_content_folder_destinations[found_platform]}content/textures/loading/robloxTilt.png")
                if os.path.exists(f"{os.path.curdir}/RobloxBrand/Original/RobloxTilt.png"):
                    copyFile(f"{os.path.curdir}/RobloxBrand/Original/RobloxTilt.png", f"{stored_content_folder_destinations[found_platform]}content/textures/loading/robloxTiltRed.png")
                printSuccessMessage("Successfully changed current app icon! It may take a moment for macOS to identify it!")

        if main_os == "Darwin":
            if os.path.exists("/Applications/Roblox.app/Contents/Info.plist"):
                plist_data = handler.readPListFile("/Applications/Roblox.app/Contents/Info.plist")
                if plist_data.get("CFBundleName"):
                    printMainMessage("Editing Roblox Info.plist..")
                    if (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True):
                        if plist_data.get("LSMultipleInstancesProhibited"):
                            plist_data["LSMultipleInstancesProhibited"] = False
                    else:
                        if plist_data.get("LSMultipleInstancesProhibited"):
                            plist_data["LSMultipleInstancesProhibited"] = True
                    if plist_data.get("CFBundleURLTypes"):
                        plist_data["CFBundleURLTypes"] = []
                    s = handler.writePListFile("/Applications/Roblox.app/Contents/Info.plist", plist_data)
                    if s["success"] == True:
                        printSuccessMessage("Successfully wrote to Info.plist!")
                    else:
                        printErrorMessage(f"Something went wrong saving Roblox Info.plist: {s['message']}")
    prepareRoblox()
    printMainMessage("Installing Fast Flags..")
    if loadedJSON == True:
        if not (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True):
            if handler.getIfRobloxIsOpen():
                handler.endRoblox()
            handler.installFastFlagsJSON(fastFlagConfig, debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
        else:
            handler.installFastFlagsJSON(fastFlagConfig, debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True), endRobloxInstances=False)
    else:
        printErrorMessage("There was an error reading your configuration file.")
    mod_mode_module = None
    mod_mode_json = None
    if fastFlagConfig.get("EFlagEnableModModes") == True:
        if fastFlagConfig.get("EFlagSelectedModMode") and fastFlagConfig.get("EFlagEnableModModeScripts") == True and os.path.exists(os.path.join(os.path.curdir, "ModModes", fastFlagConfig.get("EFlagSelectedModMode"), "ModScript.py")):
            if os.path.exists(os.path.join(os.path.curdir, "ModModes", fastFlagConfig.get("EFlagSelectedModMode"), "Manifest.json")):
                mod_mode_json = readJSONFile(f"./ModModes/{fastFlagConfig.get('EFlagSelectedModMode')}/Manifest.json")
                if mod_mode_json:
                    if mod_mode_json.get("mod_script") == True:
                        printMainMessage("Preparing Mod Mode Script..")
                        script_path = os.path.join(os.path.curdir, "ModModes", fastFlagConfig.get("EFlagSelectedModMode"), "ModScript.py")
                        try:
                            spec = importlib.util.spec_from_file_location("ModScript", script_path)
                            mod_mode_module = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(mod_mode_module)
                            printSuccessMessage("Successfully connected to script!")
                        except Exception as e:
                            printDebugMessage(f"Error from mod mode module: {str(e)}")
                            printErrorMessage("Something went wrong with loading the mod mode module!")
    printSuccessMessage("Done! Roblox is ready!")
    printWarnMessage("--- Running Roblox ---")
    setTypeOfServer = 0
    rpc = None
    rpc_info = None
    set_current_private_server_key = None
    current_place_info = None
    is_teleport = False
    updated_count = 0

    def onGameJoined(info):
        if info.get("ip"):
            printDebugMessage(f"Roblox IP Address Detected! IP: {info.get("ip")}")
            allocated_roblox_ip = info.get("ip")
            generated_location = "Unknown Location"
            try:
                import requests
            except Exception as e:
                pip().install(["requests"])
                import requests
                printSuccessMessage("Successfully installed modules!")
            server_info_res = requests.get(f"https://ipinfo.io/{allocated_roblox_ip}/json")
            if server_info_res.ok:
                server_info_json = server_info_res.json()
                if server_info_json.get("city") and server_info_json.get("country"):
                    if not (server_info_json.get("region") == None or server_info_json.get("region") == ""):
                        generated_location = f"{server_info_json['city']}, {server_info_json['region']}, {server_info_json['country']}"
                    else:
                        generated_location = f"{server_info_json['city']}, {server_info_json['country']}"
                else:
                    if fastFlagConfig.get("EFlagEnableDebugMode"): printDebugMessage(server_info_res.text)
                    printDebugMessage("Failed to get server information: IP Request resulted with no information.")
            else:
                if fastFlagConfig.get("EFlagEnableDebugMode"): printDebugMessage(server_info_res.text)
                printDebugMessage("Failed to get server information: IP Request Rejected.")

            if fastFlagConfig.get("EFlagNotifyServerLocation") == True:
                printSuccessMessage(f"Roblox is connecting to a server in: {generated_location} [{allocated_roblox_ip}]")
                if setTypeOfServer == 0:
                    displayNotification("Joining Server", f"You have connected to a server from {generated_location}!")
                elif setTypeOfServer == 1:
                    displayNotification("Joining Private Server", f"You have connected to a private server from {generated_location}!")
                elif setTypeOfServer == 2:
                    displayNotification("Joining Reserved Server", f"You have connected to a reserved server from {generated_location}!")
                elif setTypeOfServer == 3:
                    displayNotification("Joining Party", f"You have connected to a party server from {generated_location}!")
                else:
                    displayNotification("Joining Server", f"You have connected to a server from {generated_location}!")
                printDebugMessage("Sent Notification to Bootstrap for Notification Center shipping!")

            global current_place_info
            if current_place_info:
                current_place_info["server_location"] = generated_location

                generated_universe_id_res = requests.get(f"https://apis.roblox.com/universes/v1/places/{current_place_info.get('placeId')}/universe")
                if generated_universe_id_res.ok:
                    generated_universe_id_json = generated_universe_id_res.json()
                    if generated_universe_id_json and not (generated_universe_id_json.get("universeId") == None):
                        current_place_info["universeId"] = generated_universe_id_json.get("universeId")
                    else:
                        current_place_info = None
                else:
                    current_place_info = None
                if current_place_info:
                    generated_thumbnail_api_url = f"https://thumbnails.roblox.com/v1/games/icons?universeIds={current_place_info['universeId']}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false"
                    generated_place_api_url = f"https://games.roblox.com/v1/games?universeIds={current_place_info['universeId']}"
                    generated_thumbnail_api_res = requests.get(generated_thumbnail_api_url)
                    generated_place_api_res = requests.get(generated_place_api_url)

                    if generated_thumbnail_api_res.ok and generated_place_api_res.ok:
                        generated_thumbnail_api_json = generated_thumbnail_api_res.json()
                        generated_place_api_json = generated_place_api_res.json()

                        thumbnail_url = "https://raw.githubusercontent.com/EfazDev/roblox-bootstrap/main/BootstrapImages/DiscordIcon.png"
                        if generated_thumbnail_api_json.get("data"):
                            if len(generated_thumbnail_api_json.get("data")) > 0:
                                thumbnail_url = generated_thumbnail_api_json.get("data")[0]["imageUrl"]
                        if current_place_info:
                            current_place_info["thumbnail_url"] = thumbnail_url

                        if len(generated_place_api_json.get("data")) > 0:
                            generated_place_api_json = generated_place_api_json.get("data")[0]
                            if current_place_info:
                                current_place_info["place_info"] = generated_place_api_json
                            try:
                                start_time = datetime.datetime.now(tz=datetime.UTC).timestamp()
                                if current_place_info:
                                    current_place_info["start_time"] = start_time
                                if fastFlagConfig.get("EFlagEnableDiscordRPC") == True:
                                    try:
                                        from DiscordPresenceHandler import Presence
                                        import requests
                                    except Exception as e:
                                        pip().install(["pypresence", "requests"])
                                        from DiscordPresenceHandler import Presence
                                        import requests
                                        printSuccessMessage("Successfully installed presence modules!")
                                    global rpc
                                    need_new_rpc = True
                                    try: 
                                        if rpc and rpc.connected == True:
                                            need_new_rpc = False
                                    except Exception as e:
                                        printDebugMessage(f"There was an error setting your Discord Embed: {str(e)}")
                                    if need_new_rpc == True:
                                        rpc = Presence("1005469189907173486")
                                        rpc.connect()
                                    def embed():
                                        try:
                                            global rpc
                                            global rpc_info
                                            global set_current_private_server_key

                                            err_count = 0
                                            job_id = rpc.generate_job_id()
                                            while True:
                                                if (not rpc) or (not rpc.connected) or (not rpc.current_job_id == job_id):
                                                    break
                                                if rpc_info == None:
                                                    rpc_info = {}
                                                formatted_info = {
                                                    "details": rpc_info.get("details") if rpc_info.get("details") else f"Playing {generated_place_api_json['name']}",
                                                    "state": rpc_info.get("state") if rpc_info.get("state") else f"Made by {generated_place_api_json['creator']['name']}!",
                                                    "start": rpc_info.get("start") if rpc_info.get("start") else start_time,
                                                    "stop": rpc_info.get("stop") if rpc_info.get("stop") and rpc_info.get("stop") > 1000 else None,
                                                    "large_image": rpc_info.get("large_image") if rpc_info.get("large_image") else thumbnail_url,
                                                    "large_text": rpc_info.get("large_text") if rpc_info.get("large_text") else generated_place_api_json['name'],
                                                    "launch_data": rpc_info.get("launch_data") if rpc_info.get("launch_data") else ""
                                                }
                                                launch_data = ""
                                                add_exam = False
                                                if not formatted_info["launch_data"] == "":
                                                    formatted_info["launch_data"] = f"&launchData={formatted_info['launch_data']}"
                                                    add_exam = False
                                                if (setTypeOfServer == 1 or setTypeOfServer == 2 or setTypeOfServer == 3) and fastFlagConfig.get("EFlagAllowPrivateServerJoining") == True and set_current_private_server_key:
                                                    if add_exam == True:
                                                        launch_data = f'{launch_data}?gameInstanceId={current_place_info["jobId"]}?accessCode={set_current_private_server_key}'
                                                    else:
                                                        launch_data = f'{launch_data}&gameInstanceId={current_place_info["jobId"]}&accessCode={set_current_private_server_key}'
                                                else:
                                                    if add_exam == True:
                                                        launch_data = f'{launch_data}?gameInstanceId={current_place_info["jobId"]}'
                                                    else:
                                                        launch_data = f'{launch_data}&gameInstanceId={current_place_info["jobId"]}'
                                                formatted_info["launch_data"] = launch_data
                                                try:
                                                    isInstance = False
                                                    if formatted_info.get("start") and formatted_info.get("end"):
                                                        isInstance = True
                                                    if rpc:
                                                        try:
                                                            if fastFlagConfig.get("EFlagEnableDiscordRPCJoining") == True:
                                                                req = rpc.update(
                                                                    job_id=job_id, 
                                                                    details=formatted_info["details"], 
                                                                    state=formatted_info["state"], 
                                                                    start=formatted_info["start"], 
                                                                    end=formatted_info["stop"], 
                                                                    large_image=formatted_info["large_image"], 
                                                                    large_text=formatted_info["large_text"], 
                                                                    instance=isInstance, 
                                                                    small_image="https://raw.githubusercontent.com/EfazDev/roblox-bootstrap/main/BootstrapImages/DiscordIcon.png", 
                                                                    small_text="Efaz's Roblox Bootstrap", 
                                                                    buttons=[
                                                                        {
                                                                            "label": "Join Server! 🚀",
                                                                            "url": f"roblox://experiences/start?placeId={current_place_info['placeId']}{formatted_info['launch_data']}"
                                                                        }, 
                                                                        {
                                                                            "label": "Open Game Page 🌐", 
                                                                            "url": f"https://www.roblox.com/games/{current_place_info['placeId']}"
                                                                        }
                                                                    ]
                                                                )
                                                            else:
                                                                req = rpc.update(
                                                                    job_id=job_id, 
                                                                    details=formatted_info["details"], 
                                                                    state=formatted_info["state"], 
                                                                    start=formatted_info["start"], 
                                                                    end=formatted_info["stop"], 
                                                                    large_image=formatted_info["large_image"], 
                                                                    large_text=formatted_info["large_text"], 
                                                                    instance=isInstance, 
                                                                    small_image="https://raw.githubusercontent.com/EfazDev/roblox-bootstrap/main/BootstrapImages/DiscordIcon.png", 
                                                                    small_text="Efaz's Roblox Bootstrap", 
                                                                    buttons=[{
                                                                        "label": "Open Game Page 🌐", 
                                                                        "url": f"https://www.roblox.com/games/{current_place_info['placeId']}"
                                                                    }]
                                                                )
                                                            if req.get("code") == 2:
                                                                break
                                                        except Exception as e:
                                                            if err_count > 9:
                                                                printDebugMessage("Discord RPC Session may be broken. Loop has been broken.")
                                                                break
                                                            else:
                                                                err_count += 1
                                                except Exception as e:
                                                    if err_count > 9:
                                                        printDebugMessage("Discord RPC Session may be broken. Loop has been broken.")
                                                        break
                                                    else:
                                                        err_count += 1
                                                        printDebugMessage(f"There was an error setting your Discord Embed: {str(e)}")
                                                time.sleep(0.1)
                                        except Exception as e:
                                            printDebugMessage(f"There was an error setting your Discord Embed: {str(e)}")
                                    embed_thread = threading.Thread(target=embed)
                                    embed_thread.daemon = True
                                    embed_thread.start()
                                    printDebugMessage("Successfully attached Discord RPC!")
                                if fastFlagConfig.get("EFlagUseDiscordWebhook") == True and fastFlagConfig.get("EFlagDiscordWebhookConnect") == True:
                                    try:
                                        import requests
                                    except Exception as e:
                                        pip().install(["requests"])
                                        import requests
                                        printSuccessMessage("Successfully installed modules!")
                                    if fastFlagConfig.get("EFlagDiscordWebhookURL"):
                                        title = "Joined Server!"
                                        if setTypeOfServer == 0:
                                            title = "Joined Public Server!"
                                        elif setTypeOfServer == 1:
                                            title = "Joined Private Server!"
                                        elif setTypeOfServer == 2:
                                            title = "Joined Reserved Server!"
                                        elif setTypeOfServer == 3:
                                            title = "Joined Party!"
                                        else:
                                            title = "Joined Server!"
                                        launch_data = ""
                                        add_exam = False
                                        if not launch_data == "":
                                            launch_data = f"&launchData={launch_data}"
                                            add_exam = False
                                        if (setTypeOfServer == 1 or setTypeOfServer == 2 or setTypeOfServer == 3) and fastFlagConfig.get("EFlagAllowPrivateServerJoining") == True and set_current_private_server_key:
                                            if add_exam == True:
                                                launch_data = f'{launch_data}?gameInstanceId={current_place_info["jobId"]}&accessCode={set_current_private_server_key}'
                                            else:
                                                launch_data = f'{launch_data}?gameInstanceId={current_place_info["jobId"]}&accessCode={set_current_private_server_key}'
                                        else:
                                            if add_exam == True:
                                                launch_data = f'{launch_data}?gameInstanceId={current_place_info["jobId"]}'
                                            else:
                                                launch_data = f'{launch_data}&gameInstanceId={current_place_info["jobId"]}'

                                        generated_body = {
                                            "content": f"<@{fastFlagConfig.get('EFlagDiscordWebhookUserId')}>",
                                            "embeds": [
                                                {
                                                    "title": title,
                                                    "color": 65280,
                                                    "fields": [
                                                        {
                                                            "name": "Connected Game",
                                                            "value": f"[{generated_place_api_json['name']}](https://www.roblox.com/games/{current_place_info.get('placeId')})",
                                                            "inline": True
                                                        },
                                                        {
                                                            "name": "Join Link",
                                                            "value": f"[Join Now!](https://rbx.efaz.dev/join?placeId={current_place_info.get('placeId')}{launch_data})",
                                                            "inline": True
                                                        },
                                                        {
                                                            "name": "Started",
                                                            "value": f"<t:{int(start_time)}:R>",
                                                            "inline": True
                                                        },
                                                        {
                                                            "name": "Server Location",
                                                            "value": f"{generated_location}",
                                                            "inline": True
                                                        }
                                                    ],
                                                    "author": {
                                                        "name": "Efaz's Roblox Bootstrap",
                                                        "icon_url": "https://raw.githubusercontent.com/EfazDev/roblox-bootstrap/main/BootstrapImages/DiscordIcon.png"
                                                    },
                                                    "thumbnail": {
                                                        "url": thumbnail_url
                                                    }
                                                }
                                            ],
                                            "attachments": []
                                        }
                                        try:
                                            req = requests.post(fastFlagConfig.get("EFlagDiscordWebhookURL"), json=generated_body)
                                            if req.ok:
                                                printDebugMessage("Successfully sent webhook!")
                                            else:
                                                printErrorMessage("There was an issue sending your webhook message. Is it valid?")
                                        except Exception as e:
                                            printErrorMessage("There was an issue sending your webhook message. Is it valid?")
                            except Exception as e:
                                rpc = None
                                printDebugMessage("Unable to insert Discord Rich Presence. Please make sure Discord is open.")
                        else:
                            printDebugMessage("Provided place info is not found.")
                    else:
                        printDebugMessage(f"Place responses rejected by Roblox. [{generated_thumbnail_api_res.ok},{generated_thumbnail_api_res.status_code} | {generated_place_api_res.ok},{generated_place_api_res.status_code}]")
    def onGameStart(info):
        global current_place_info
        if info.get("placeId") and info.get("jobId"):
            current_place_info = info
    def onGameDisconnected(info):
        global current_place_info
        global is_teleport
        it_is_teleport = False
        synced_place_info = None
        if current_place_info:
            synced_place_info = current_place_info
            current_place_info = None
        if is_teleport == True:
            printYellowMessage("User has been teleported!")
            it_is_teleport = True
            is_teleport = False
        else:
            printErrorMessage("User has disconnected from the server!")
        if fastFlagConfig.get("EFlagUseDiscordWebhook") == True and fastFlagConfig.get("EFlagDiscordWebhookDisconnect") == True:
            try:
                import requests
            except Exception as e:
                pip().install(["requests"])
                import requests
                printSuccessMessage("Successfully installed modules!")
            if fastFlagConfig.get("EFlagDiscordWebhookURL"):
                thumbnail_url = "https://raw.githubusercontent.com/EfazDev/roblox-bootstrap/main/BootstrapImages/DiscordIcon.png"
                server_location = "Unknown Location"
                start_time = 0
                place_info = {"name": "???"}

                if synced_place_info:
                    if synced_place_info.get("start_time"):
                        start_time = synced_place_info.get("start_time")
                    if synced_place_info.get("server_location"):
                        server_location = synced_place_info.get("server_location")
                    if synced_place_info.get("place_info"):
                        place_info = synced_place_info.get("place_info")
                    if synced_place_info.get("thumbnail_url"):
                        thumbnail_url = synced_place_info.get("thumbnail_url")

                    server_type = "Public Server"
                    if setTypeOfServer == 0:
                        server_type = "Public Server"
                    elif setTypeOfServer == 1:
                        server_type = "Private Server"
                    elif setTypeOfServer == 2:
                        server_type = "Reserved Server"
                    elif setTypeOfServer == 3:
                        server_type = "Party"
                    else:
                        server_type = "Public Server"

                    title = f"Disconnected from {server_type}!"
                    color = 16711680

                    if it_is_teleport == True:
                        title = f"Teleported to {server_type}!"
                        color = 16776960

                    launch_data = ""
                    add_exam = False
                    if not launch_data == "":
                        launch_data = f"&launchData={launch_data}"
                        add_exam = False
                    if (setTypeOfServer == 1 or setTypeOfServer == 2 or setTypeOfServer == 3) and fastFlagConfig.get("EFlagAllowPrivateServerJoining") == True and set_current_private_server_key:
                        if add_exam == True:
                            launch_data = f'{launch_data}?gameInstanceId={synced_place_info["jobId"]}?accessCode={set_current_private_server_key}'
                        else:
                            launch_data = f'{launch_data}&gameInstanceId={synced_place_info["jobId"]}&accessCode={set_current_private_server_key}'
                    else:
                        if add_exam == True:
                            launch_data = f'{launch_data}?gameInstanceId={synced_place_info["jobId"]}'
                        else:
                            launch_data = f'{launch_data}&gameInstanceId={synced_place_info["jobId"]}'

                    generated_body = {
                        "content": f"<@{fastFlagConfig.get('EFlagDiscordWebhookUserId')}>",
                        "embeds": [
                            {
                                "title": title,
                                "color": color,
                                "fields": [
                                    {
                                        "name": "Disconnected Game",
                                        "value": f"[{place_info['name']}](https://www.roblox.com/games/{synced_place_info.get('placeId')})",
                                        "inline": True
                                    },
                                    {
                                        "name": "Join Link",
                                        "value": f"[Join Again!](https://rbx.efaz.dev/join?placeId={synced_place_info.get('placeId')}{launch_data})",
                                        "inline": True
                                    },
                                    {
                                        "name": "Started",
                                        "value": f"<t:{int(start_time)}:R>",
                                        "inline": True
                                    },
                                    {
                                        "name": "Server Location",
                                        "value": f"{server_location}",
                                        "inline": True
                                    },
                                    {
                                        "name": "Closing Reason",
                                        "value": f"{info.get('message')} (Code: {info.get('code')})",
                                        "inline": True
                                    }
                                ],
                                "author": {
                                    "name": "Efaz's Roblox Bootstrap",
                                    "icon_url": "https://raw.githubusercontent.com/EfazDev/roblox-bootstrap/main/BootstrapImages/DiscordIcon.png"
                                },
                                "thumbnail": {
                                    "url": thumbnail_url
                                }
                            }
                        ],
                        "attachments": []
                    }
                    try:
                        req = requests.post(fastFlagConfig.get("EFlagDiscordWebhookURL"), json=generated_body)
                        if req.ok:
                            printDebugMessage("Successfully sent webhook!")
                        else:
                            printErrorMessage("There was an issue sending your webhook message. Is it valid?")
                    except Exception as e:
                        printErrorMessage("There was an issue sending your webhook message. Is it valid?")
        if fastFlagConfig.get("EFlagEnableDiscordRPC") == True:
            global rpc
            global rpc_info
            try: 
                if rpc:
                    rpc.clear()
            except Exception as e:
                printDebugMessage(f"There was an error setting your Discord Embed: {str(e)}")
            rpc_info = None
    def onTeleport(consoleLine):
        global is_teleport
        is_teleport = True
    def onBloxstrapMessage(info):
        if fastFlagConfig.get("EFlagAllowBloxstrapSDK") == True:
            printMainMessage("Received Bloxstrap Message!")
            global rpc
            global rpc_info
            if info.get("command"):
                if info["command"] == "SetRichPresence":
                    if rpc:
                        if rpc_info == None:
                            rpc_info = {}
                        if type(info["data"]) is dict:
                            if type(info["data"].get("details")) is str or type(info["data"].get("details")) is None: rpc_info["details"] = info["data"].get("details")
                            if type(info["data"].get("state")) is str or type(info["data"].get("state")) is None: rpc_info["state"] = info["data"].get("state")
                            if type(info["data"].get("timeStart")) is int or type(info["data"].get("timeStart")) is None or type(info["data"].get("timeStart")) is float: rpc_info["start"] = info["data"].get("timeStart")
                            if type(info["data"].get("timeEnd")) is int or type(info["data"].get("timeEnd")) is None or type(info["data"].get("timeEnd")) is float: rpc_info["stop"] = info["data"].get("timeEnd")
                            if type(info["data"].get("largeImage")) is dict: 
                                if type(info["data"]["largeImage"].get("assetId")) is int: rpc_info["large_image"] = f'https://assetdelivery.roblox.com/v1/asset/?id={info["data"]["largeImage"]["assetId"]}'
                                if type(info["data"]["largeImage"].get("hoverText")) is str: rpc_info["large_text"] = info["data"]["largeImage"]["hoverText"]
                            elif type(info["data"].get("largeImage")) is None:
                                rpc_info["large_image"] = None
                                rpc_info["large_text"] = None
                elif info["command"] == "SetLaunchData":
                    if rpc:
                        if rpc_info == None:
                            rpc_info = {}
                        if type(info["data"]) is str: rpc_info["launch_data"] = info["data"].get("launch_data")
    def onRobloxExit(consoleLine):
        printDebugMessage("User has closed the Roblox window!")
        printErrorMessage("Roblox window was closed! Closing Bootstrap App..")
        if fastFlagConfig.get("EFlagEnableDiscordRPC") == True:
            global rpc
            global rpc_info
            global current_place_info
            try: 
                if rpc: rpc.close()
            except Exception as e:
                printDebugMessage(f"There was an error setting your Discord Embed: {str(e)}")
            rpc = None
            rpc_info = None
            current_place_info = None
        sys.exit(0)
    def onRobloxCrash(consoleLine):
        global updated_count
        updated_count = 999
        printErrorMessage("There was an error inside the RobloxPlayer that has caused it to crash! Sorry!")
        printDebugMessage(f"Crashed Data: {consoleLine}")
    def onAllRobloxEvents(data):
        if fastFlagConfig.get("EFlagEnableModModes") == True:
            if fastFlagConfig.get("EFlagSelectedModMode") and fastFlagConfig.get("EFlagEnableModModeScripts") == True and os.path.exists(os.path.join(os.path.curdir, "ModModes", fastFlagConfig.get("EFlagSelectedModMode"), "ModScript.py")):
                if os.path.exists(os.path.join(os.path.curdir, "ModModes", fastFlagConfig.get("EFlagSelectedModMode"), "Manifest.json")):
                    if mod_mode_json:
                        if mod_mode_json.get("mod_script") == True:
                            try:
                                if type(fastFlagConfig.get("EFlagModModeAllowedDetectments")) is list:
                                    if "onRobloxLog" in fastFlagConfig.get("EFlagModModeAllowedDetectments"):
                                        if hasattr(mod_mode_module, "onRobloxLog"):
                                            threading.Thread(target=getattr(mod_mode_module, "onRobloxLog"), args=[data]).start()
                                    if data.get("eventName") in fastFlagConfig.get("EFlagModModeAllowedDetectments"):
                                        if hasattr(mod_mode_module, data.get("eventName")):
                                            threading.Thread(target=getattr(mod_mode_module, data.get("eventName")), args=[data["data"]]).start()
                            except Exception as e:
                                printDebugMessage(f"Unable to run mod mode script: {str(e)}")

    def onPrivateServer(data):
        global setTypeOfServer
        global set_current_private_server_key
        setTypeOfServer = 1
        if fastFlagConfig.get("EFlagAllowPrivateServerJoining") == True and data and data.get("data"):
            set_current_private_server_key = data["data"].get("accessCode")
        else:
            set_current_private_server_key = None
        printSuccessMessage("Roblox is currently pending to a private server!")
    def onReservedServer(data):
        global setTypeOfServer
        global set_current_private_server_key
        setTypeOfServer = 2
        if fastFlagConfig.get("EFlagAllowPrivateServerJoining") == True and data and data.get("data"):
            set_current_private_server_key = data["data"].get("accessCode")
        else:
            set_current_private_server_key = None
        printSuccessMessage("Roblox is currently pending to a reserved server!")
    def onPartyServer(data):
        global setTypeOfServer
        global set_current_private_server_key
        setTypeOfServer = 3
        if fastFlagConfig.get("EFlagAllowPrivateServerJoining") == True and data and data.get("data"):
            set_current_private_server_key = data["data"].get("accessCode")
        else:
            set_current_private_server_key = None
        printSuccessMessage("Roblox is currently pending to a party!")
    def onMainServer(consoleLine):
        global setTypeOfServer
        global set_current_private_server_key
        setTypeOfServer = 0
        set_current_private_server_key = None
        printSuccessMessage("Roblox is currently pending to a public server!")
    
    def runRoblox():
        if makeAnotherRoblox == True:
            printDebugMessage(f"Opening extra Roblox window..")
            clas = handler.openRoblox(makeDupe=True, debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True), attachInstance=(not (fastFlagConfig.get("EFlagAllowActivityTracking") == False)), allowRobloxOtherLogDebug=(fastFlagConfig.get("EFlagAllowFullDebugMode") == True))
            if clas:
                clas.setRobloxEventCallback("onRobloxExit", onRobloxExit)
                clas.setRobloxEventCallback("onRobloxCrash", onRobloxCrash)
                clas.setRobloxEventCallback("onRobloxLog", onAllRobloxEvents)
                clas.setRobloxEventCallback("onBloxstrapSDK", onBloxstrapMessage)
                clas.setRobloxEventCallback("onGameStart", onGameStart)
                clas.setRobloxEventCallback("onGameJoined", onGameJoined)
                clas.setRobloxEventCallback("onGameDisconnected", onGameDisconnected)
                clas.setRobloxEventCallback("onGameLoading", onMainServer)
                clas.setRobloxEventCallback("onGameLoadingPrivate", onPrivateServer)
                clas.setRobloxEventCallback("onGameLoadingReserved", onReservedServer)
                clas.setRobloxEventCallback("onGameLoadingParty", onPartyServer)
                clas.setRobloxEventCallback("onGameTeleport", onTeleport)
                printSuccessMessage("Connected to Roblox Instance from log file for Activity Tracking!")
            else:
                printDebugMessage("No RobloxInstance class was registered")
            check_update_thread = threading.Thread(target=checkIfUpdateWasNeeded)
            check_update_thread.start()
        elif len(given_args) > 1:
            if main_os == "Darwin":
                url_str = unquote(given_args[1])
                if url_str:
                    url = unquote(url_str)
            elif main_os == "Windows":
                url = given_args[1]
            if url:
                if ("roblox-player:" in url) or ("roblox:" in url) or ("efaz-bootstrap" in url and "continue" in url) or ("efaz-bootstrap" in url and "new" in url) or ("efaz-bootstrap" in url and "menu" in url):
                    printDebugMessage(f"Running using Roblox URL: {url}")
                    clas = handler.openRoblox(forceQuit=(not (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True)), makeDupe=(fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True), debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True), startData=url, attachInstance=(not (fastFlagConfig.get("EFlagAllowActivityTracking") == False)), allowRobloxOtherLogDebug=(fastFlagConfig.get("EFlagAllowFullDebugMode") == True))
                    if clas:
                        clas.setRobloxEventCallback("onRobloxExit", onRobloxExit)
                        clas.setRobloxEventCallback("onRobloxCrash", onRobloxCrash)
                        clas.setRobloxEventCallback("onRobloxLog", onAllRobloxEvents)
                        clas.setRobloxEventCallback("onBloxstrapSDK", onBloxstrapMessage)
                        clas.setRobloxEventCallback("onGameStart", onGameStart)
                        clas.setRobloxEventCallback("onGameJoined", onGameJoined)
                        clas.setRobloxEventCallback("onGameDisconnected", onGameDisconnected)
                        clas.setRobloxEventCallback("onGameLoading", onMainServer)
                        clas.setRobloxEventCallback("onGameLoadingPrivate", onPrivateServer)
                        clas.setRobloxEventCallback("onGameLoadingReserved", onReservedServer)
                        clas.setRobloxEventCallback("onGameLoadingParty", onPartyServer)
                        clas.setRobloxEventCallback("onGameTeleport", onTeleport)
                        printSuccessMessage("Connected to Roblox Instance from log file for Activity Tracking!")
                    else:
                        printDebugMessage("No RobloxInstance class was registered")
                    check_update_thread = threading.Thread(target=checkIfUpdateWasNeeded)
                    check_update_thread.start()
                else:
                    printDebugMessage(f"Unknown scheme: {url}")
        else:
            if handler.getIfRobloxIsOpen():
                printMainMessage("An existing Roblox Window is currently open. Would you like to restart it in order for changes to take effect?")
                c = input("> ")
                if isYes(c) == True:
                    handler.endRoblox()
                else:
                    os.system("exit")
                    exit()
            clas = handler.openRoblox(forceQuit=(not (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True)), debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True), attachInstance=(not (fastFlagConfig.get("EFlagAllowActivityTracking") == False)), allowRobloxOtherLogDebug=(fastFlagConfig.get("EFlagAllowFullDebugMode") == True))
            if clas:
                clas.setRobloxEventCallback("onRobloxExit", onRobloxExit)
                clas.setRobloxEventCallback("onRobloxCrash", onRobloxCrash)
                clas.setRobloxEventCallback("onRobloxLog", onAllRobloxEvents)
                clas.setRobloxEventCallback("onBloxstrapSDK", onBloxstrapMessage)
                clas.setRobloxEventCallback("onGameStart", onGameStart)
                clas.setRobloxEventCallback("onGameJoined", onGameJoined)
                clas.setRobloxEventCallback("onGameDisconnected", onGameDisconnected)
                clas.setRobloxEventCallback("onGameLoading", onMainServer)
                clas.setRobloxEventCallback("onGameLoadingPrivate", onPrivateServer)
                clas.setRobloxEventCallback("onGameLoadingReserved", onReservedServer)
                clas.setRobloxEventCallback("onGameLoadingParty", onPartyServer)
                clas.setRobloxEventCallback("onGameTeleport", onTeleport)
                printSuccessMessage("Connected to Roblox Instance from log file for Activity Tracking!")
            else:
                printDebugMessage("No RobloxInstance class was registered")
            check_update_thread = threading.Thread(target=checkIfUpdateWasNeeded)
            check_update_thread.start()
    def checkIfUpdateWasNeeded():
        global updated_count
        updated_count += 1
        if updated_count < 3:
            printMainMessage("Waiting 2 seconds to check if Roblox needs a reinstall..")
            time.sleep(2)
            if not (handler.getIfRobloxIsOpen()):
                printMainMessage("An update is needed. Installing a fresh copy of Roblox!")
                handler.installRoblox(forceQuit=(not (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True)), debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
                time.sleep(1)
                prepareRoblox()
                time.sleep(2)
                runRoblox()
            else:
                printSuccessMessage("Roblox doesn't require any updates!")
        else:
            printErrorMessage("Is Roblox crashing instantly..? Well, ending script here.")
    runRoblox()
    os.system("exit")
    exit()