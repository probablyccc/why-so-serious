import os
import shutil
import json
import sys
import platform
import subprocess
import time
import RobloxFastFlagsInstaller

if __name__ == "__main__":
    main_os = platform.system()
    windows_dir = f"{os.getenv('LOCALAPPDATA')}\\Roblox"

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
    currentVersion = {"version": "1.0.2"}

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
        a = shutil.copy(pa, de)
        printDebugMessage(f"Copied File: {pa} => {de}")
        return a
    
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
        if main_os == "Windows":
            os.system(f"py RobloxFastFlagsInstaller.py")
        elif main_os == "Darwin":
            os.system(f"python3 RobloxFastFlagsInstaller.py")

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

        printWarnMessage("Installer finished! Would you like to continue to Roblox? (y/n)")
        a = input("> ")
        if isYes(a) == False:
            exit()

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

        printMainMessage("Would you like to change the client's icon set (may work)? (y/n)")
        b = input("> ")
        if isYes(b) == True:
            fastFlagConfig["EFlagEnableChangeIconSet"] = True
            def scan_name(a):
                if main_os == "Windows":
                    if os.path.exists(f"{os.path.curdir}\\IconSets\\{a}\\"):
                        return True
                    else:
                        return False
                elif main_os == "Darwin":
                    if os.path.exists(f"{os.path.curdir}/IconSets/{a}/"):
                        return True
                    else:
                        return False
            def getName():
                got_set = []
                for i in os.listdir("./IconSets/"):
                    if os.path.isdir(f"./IconSets/{i}/"):
                        got_set.append(i)
                printWarnMessage("Select the number that is associated with the icons you want to use.")
                got_set = sorted(got_set)
                count = 1
                for i in got_set:
                    printMainMessage(f"[{str(count)}] = {i}")
                    count += 1
                if main_os == "Darwin":
                    printYellowMessage("[Also, if you just added a new icon folder into the IconSets folder, please rerun Install.py in order for it to seen.]")
                a = input("> ")
                if a.isnumeric():
                    c = int(a)-1
                    if c < len(got_set) and c >= 0:
                        if got_set[c]:
                            b = got_set[c]
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
            set_icon_set = getName()
            fastFlagConfig["EFlagSelectedIconSet"] = set_icon_set
            printSuccessMessage(f"Set icon set: {set_icon_set}")
        elif isNo(b) == True:
            fastFlagConfig["EFlagEnableChangeIconSet"] = False
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

        printMainMessage("Would you like to enable Debug Mode? (y/n)")
        printYellowMessage("[WARNING! This will expose information like login to Roblox and will reduce speed.]")
        d = input("> ")
        if isYes(d) == True:
            fastFlagConfig["EFlagEnableDebugMode"] = True
            printDebugMessage("User selected: True")
        elif isNo(d) == True:
            fastFlagConfig["EFlagEnableDebugMode"] = False
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
        printWarnMessage("Settings finished! Would you like to continue to Roblox? (y/n)")
        a = input("> ")
        if isYes(a) == False:
            exit()

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
        printWarnMessage("Sync finished! Would you like to continue to Roblox? (y/n)")
        a = input("> ")
        if isYes(a) == False:
            exit()

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
        printWarnMessage("Sync finished! Would you like to continue to Roblox? (y/n)")
        a = input("> ")
        if isYes(a) == False:
            exit()

    def handleOption7():
        printWarnMessage("--- Credits ---")
        printMainMessage("1. Main Coding by \033[38;5;202m@EfazDev\033[0m")
        printMainMessage("2. Old Death Sound and Cursors were sourced from \033[38;5;165mBloxstrap files (https://github.com/pizzaboxer/bloxstrap)\033[0m")
        printMainMessage("3. AvatarEditorMaps were from \033[38;5;197mMielesgames's Map Files (https://github.com/Mielesgames/RobloxAvatarEditorMaps)\033[0m slightly edited to be usable for the current version of Roblox (as of the time of writing this)")
        printMainMessage("4. Some files were exported from the main macOS Roblox.app files. \033[38;5;202m(Logo was made using the Apple Pages icon, hued and then added the Roblox Logo)\033[0m")
        printMainMessage("5. macOS App was built using \033[38;5;39mpyinstaller\033[0m. You can recreate and deploy using this command: \033[38;5;39mpyinstaller EfazRobloxBootstrap.spec --distpath Apps --noconfirm && rm -rf build ./Apps/EfazRobloxBootstrap/ && python3 Install.py\033[0m")
        printDebugMessage(f"Operating System: {main_os}")
        printDebugMessage(f"Debug Mode Enabled")
        printWarnMessage("Would you like to continue to Roblox? (y/n)")
        a = input("> ")
        if isYes(a) == False:
            exit()

    def handleOption8():
        printWarnMessage("--- End All Roblox Instances ---")
        printMainMessage("Are you sure you want to end all currently open Roblox instances?")
        a = input("> ")
        if isYes(a) == True:
            handler.endRoblox()

        printWarnMessage("Option finished! Would you like to continue to Roblox? (y/n)")
        a = input("> ")
        if isYes(a) == False:
            exit()

    def handleOption9():
        printWarnMessage("--- Reinstall Roblox ---")
        printMainMessage("Are you sure you want to reinstall Roblox?")
        a = input("> ")
        if isYes(a) == True:
            handler.installRoblox()

        printWarnMessage("Option finished! Would you like to continue to Roblox? (y/n)")
        a = input("> ")
        if isYes(a) == False:
            exit()

    if len(sys.argv) < 2:
        if not (fastFlagConfig.get("EFlagSkipEfazRobloxBootstrapPromptUI") == True):
            generated_ui_options = []
            main_ui_options = {}
            generated_ui_options.append({"index": 1, "message": "Continue to Roblox", "func": handleOption1})
            generated_ui_options.append({"index": 3, "message": "Run Fast Flag Installer", "func": handleOption3})
            generated_ui_options.append({"index": 4, "message": "Set Settings", "func": handleOption4})
            generated_ui_options.append({"index": 5, "message": "End All Roblox Instances", "func": handleOption8})
            generated_ui_options.append({"index": 6, "message": "Reinstall Roblox", "func": handleOption9})
            generated_ui_options.append({"index": 99, "message": "Credits", "func": handleOption7})
            if main_os == "Darwin":
                if (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True):
                    generated_ui_options.append({"index": 2, "message": "Generate Another Roblox Instance", "func": handleOption2})
            if (fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir") and os.path.exists(fastFlagConfig.get("EFlagEfazRobloxBootStrapSyncDir"))):
                generated_ui_options.append({"index": 10, "message": "Sync to Fast Flag Configuration", "func": handleOption5})
                generated_ui_options.append({"index": 11, "message": "Sync from Fast Flag Configuration", "func": handleOption6})

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
    elif len(sys.argv) > 1 and main_os == "Darwin":
        url = sys.argv[1]
        if "efaz-bootstrap" in url:
            if "continue" in url:
                handleOption1()
            elif "new" in url:
                handleOption2()
            elif "fflag-install" in url:
                handleOption3()
            elif "settings" in url:
                handleOption4()
            elif "sync-to-install" in url:
                handleOption5()
            elif "sync-from-install" in url:
                handleOption6()
            elif "end-roblox" in url:
                handleOption8()
            elif "reinstall-roblox" in url:
                handleOption9()
            elif ("credits" in url) or ("about" in url):
                handleOption7()
            else:
                printDebugMessage(f"Unknown command: {url}")
                printWarnMessage("--- Continue to Roblox? ---")
                printMainMessage("[1] = Continue")
                printMainMessage("[2] = Revert Remove UI")
                printMainMessage("[*] = End Process")
                res = input("> ")
                if res == "1":
                    handleOption1()
                elif res == "2":
                    fastFlagConfig["EFlagSkipEfazRobloxBootstrapPromptUI"] = False
                    with open("FastFlagConfiguration.json", "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                    printSuccessMessage("Reverted successfully!")
                    input("> ")
                    exit()
                else:
                    exit()

    if (not (fastFlagConfig.get("EFlagDisableBootstrapChecks") == True)) and os.path.exists("Version.json"):
        printWarnMessage("--- Checking for Bootstrap Updates ---")
        skip_check = False
        try:
            import requests
        except Exception as e:
            import pip
            printMainMessage("Some modules are not installed. Do you want to install all the modules required now? (y/n)")
            if isYes(input("> ")) == True:
                pip.main(["install", "requests"])
                printSuccessMessage("Successfully installed modules!")
            else:
                skip_check = True
        if skip_check == False:
            latest_vers_res = requests.get("https://raw.githubusercontent.com/EfazDev/roblox-bootstrap/main/Version.json")
            if latest_vers_res.ok:
                latest_vers = latest_vers_res.json()
                if currentVersion.get("version"):
                    if currentVersion.get("version", "1.0.0") < latest_vers.get("version", "1.0.0"):
                        printMainMessage(f"Update v{latest_vers['version']} detected!")
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
                        printSuccessMessage(f"Update to v{latest_vers['version']} was finished successfully! Please restart this script!")
                        input("> ")
                        exit()
                    else:
                        printMainMessage("Running latest version of Bootstrap!")
                else:
                    printDebugMessage("Current Version Data Corrupted.")
            else:
                printDebugMessage("Update Check Response failed.")

    printWarnMessage("--- Checking for Roblox Updates ---")
    latest_version = handler.getLatestClientVersion(debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
    current_version = handler.getCurrentClientVersion()

    if fastFlagConfig.get("EFlagFreshCopyRoblox") == True:
        printWarnMessage("--- Installing Latest Roblox Version ---")
        handler.installRoblox(debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
    elif latest_version["success"] == True and current_version["success"] == True:
        if current_version["isClientVersion"] == True:
            if current_version["version"] == latest_version["client_version"]:
                printMainMessage("Running current version of Roblox!")
            else:
                printWarnMessage("--- Installing Latest Roblox Version ---")
                handler.installRoblox(debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
        else:
            if current_version["version"] == latest_version["short_version"]:
                printMainMessage("Running latest version of Roblox!")
            else:
                printWarnMessage("--- Installing Latest Roblox Version ---")
                handler.installRoblox(debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
    else:
        printErrorMessage("There was issue while checking for updates.")

    printWarnMessage("--- Preparing Roblox ---")
    def prepareRoblox():
        global main_os
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
        
        if fastFlagConfig.get("EFlagEnableChangeIconSet") == True:
            printMainMessage("Changing Icons..")
            if main_os == "Windows":
                if os.path.exists(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_color.png"): copyFile(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_color.png", f"{stored_robux_folder_destinations[found_platform]}robux_color.png")
                if os.path.exists(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_color@2x.png"): copyFile(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_color@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux_color@2x.png")
                if os.path.exists(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_color@3x.png"): copyFile(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_color@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux_color@3x.png")
                if os.path.exists(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_small.png"): copyFile(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_small.png", f"{stored_robux_folder_destinations[found_platform]}robux_small.png")
                if os.path.exists(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_small@2x.png"): copyFile(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_small@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux_small@2x.png")
                if os.path.exists(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_small@3x.png"): copyFile(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux_small@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux_small@3x.png")
                if os.path.exists(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux.png"): copyFile(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux.png", f"{stored_robux_folder_destinations[found_platform]}robux.png")
                if os.path.exists(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux@2x.png"): copyFile(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux@2x.png")
                if os.path.exists(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux@3x.png"): copyFile(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\robux@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux@3x.png")
                if os.path.exists(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\RobloxEmoji.ttf"): copyFile(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\RobloxEmoji.ttf", f"{stored_content_folder_destinations[found_platform]}content\\fonts\\RobloxEmoji.ttf")
                shutil.copytree(f"{os.path.curdir}\\IconSets\\{fastFlagConfig['EFlagSelectedIconSet']}\\", f"{stored_content_folder_destinations[found_platform]}\\", dirs_exist_ok=True)
            elif main_os == "Darwin":
                if os.path.exists(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color.png"): copyFile(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color.png", f"{stored_robux_folder_destinations[found_platform]}robux_color.png")
                if os.path.exists(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color.png"): copyFile(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux_color@2x.png")
                if os.path.exists(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color.png"): copyFile(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux_color@3x.png")
                if os.path.exists(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color.png"): copyFile(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_small.png", f"{stored_robux_folder_destinations[found_platform]}robux_small.png")
                if os.path.exists(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color.png"): copyFile(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_small@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux_small@2x.png")
                if os.path.exists(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color.png"): copyFile(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_small@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux_small@3x.png")
                if os.path.exists(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color.png"): copyFile(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux.png", f"{stored_robux_folder_destinations[found_platform]}robux.png")
                if os.path.exists(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color.png"): copyFile(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux@2x.png")
                if os.path.exists(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux_color.png"): copyFile(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/robux@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux@3x.png")
                if os.path.exists(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/RobloxEmoji.ttf"): copyFile(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/RobloxEmoji.ttf", f"{stored_content_folder_destinations[found_platform]}content/fonts/RobloxEmoji.ttf")
                shutil.copytree(f"{os.path.curdir}/IconSets/{fastFlagConfig['EFlagSelectedIconSet']}/", f"{stored_content_folder_destinations[found_platform]}/", dirs_exist_ok=True)
            printSuccessMessage("Successfully changed Current Icon Files to icon set!")
        else:
            printMainMessage("Changing Icon Set..")
            if main_os == "Windows":
                copyFile(f"{os.path.curdir}\\IconSets\\Original\\robux_color.png", f"{stored_robux_folder_destinations[found_platform]}robux_color.png")
                copyFile(f"{os.path.curdir}\\IconSets\\Original\\robux_color@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux_color@2x.png")
                copyFile(f"{os.path.curdir}\\IconSets\\Original\\robux_color@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux_color@3x.png")
                copyFile(f"{os.path.curdir}\\IconSets\\Original\\robux_small.png", f"{stored_robux_folder_destinations[found_platform]}robux_small.png")
                copyFile(f"{os.path.curdir}\\IconSets\\Original\\robux_small@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux_small@2x.png")
                copyFile(f"{os.path.curdir}\\IconSets\\Original\\robux_small@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux_small@3x.png")
                copyFile(f"{os.path.curdir}\\IconSets\\Original\\robux.png", f"{stored_robux_folder_destinations[found_platform]}robux.png")
                copyFile(f"{os.path.curdir}\\IconSets\\Original\\robux@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux@2x.png")
                copyFile(f"{os.path.curdir}\\IconSets\\Original\\robux@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux@3x.png")
                if os.path.exists(f"{os.path.curdir}\\IconSets\\Original\\RobloxEmoji.ttf"):
                    copyFile(f"{os.path.curdir}\\IconSets\\Original\\RobloxEmoji.ttf", f"{stored_content_folder_destinations[found_platform]}content\\fonts\\RobloxEmoji.ttf")
                shutil.copytree(f"{os.path.curdir}\\IconSets\\Original\\", f"{stored_content_folder_destinations[found_platform]}\\", dirs_exist_ok=True)
            elif main_os == "Darwin":
                copyFile(f"{os.path.curdir}/IconSets/Original/robux_color.png", f"{stored_robux_folder_destinations[found_platform]}robux_color.png")
                copyFile(f"{os.path.curdir}/IconSets/Original/robux_color@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux_color@2x.png")
                copyFile(f"{os.path.curdir}/IconSets/Original/robux_color@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux_color@3x.png")
                copyFile(f"{os.path.curdir}/IconSets/Original/robux_small.png", f"{stored_robux_folder_destinations[found_platform]}robux_small.png")
                copyFile(f"{os.path.curdir}/IconSets/Original/robux_small@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux_small@2x.png")
                copyFile(f"{os.path.curdir}/IconSets/Original/robux_small@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux_small@3x.png")
                copyFile(f"{os.path.curdir}/IconSets/Original/robux.png", f"{stored_robux_folder_destinations[found_platform]}robux.png")
                copyFile(f"{os.path.curdir}/IconSets/Original/robux@2x.png", f"{stored_robux_folder_destinations[found_platform]}robux@2x.png")
                copyFile(f"{os.path.curdir}/IconSets/Original/robux@3x.png", f"{stored_robux_folder_destinations[found_platform]}robux@3x.png")
                if os.path.exists(f"{os.path.curdir}/IconSets/Original/RobloxEmoji.ttf"):
                    copyFile(f"{os.path.curdir}/IconSets/Original/RobloxEmoji.ttf", f"{stored_content_folder_destinations[found_platform]}content/fonts/RobloxEmoji.ttf")
                shutil.copytree(f"{os.path.curdir}/IconSets/Original/", f"{stored_content_folder_destinations[found_platform]}/", dirs_exist_ok=True)
                
            printSuccessMessage("Successfully changed Current Icon Files to original!")

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
            printMainMessage("Editing Roblox Info.plist..")
            if (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True):
                with open("/Applications/Roblox.app/Contents/Info.plist", "r") as f:
                    plist_data = f.read()
                plist_data = plist_data.replace("LSMultipleInstancesProhibited", "LSMultipleInstancesEnabled")
                with open("/Applications/Roblox.app/Contents/Info.plist", "w") as f:
                    f.write(plist_data)
            else:
                with open("/Applications/Roblox.app/Contents/Info.plist", "r") as f:
                    plist_data = f.read()
                plist_data = plist_data.replace("LSMultipleInstancesEnabled", "LSMultipleInstancesProhibited")
                with open("/Applications/Roblox.app/Contents/Info.plist", "w") as f:
                    f.write(plist_data)
            printSuccessMessage("Successfully wrote to Info.plist!")
    
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
    printSuccessMessage("Done! Roblox is ready!")
    printWarnMessage("--- Running Roblox ---")
    def checkIfUpdateWasNeeded():
        printMainMessage("Waiting 5 seconds to check if Roblox needs a reinstall..")
        time.sleep(5)
        if not (handler.getIfRobloxIsOpen()):
            printMainMessage("An update is needed. Installing a fresh copy of Roblox!")
            handler.installRoblox(forceQuit=(not (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True)), debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
            prepareRoblox()
        else:
            printSuccessMessage("Roblox doesn't require any updates!")

    if makeAnotherRoblox == True:
        printDebugMessage(f"Opening extra Roblox window..")
        handler.openRoblox(makeDupe=True, debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
        checkIfUpdateWasNeeded()
    elif len(sys.argv) > 1 and main_os == "Darwin":
        url = sys.argv[1]
        if ("roblox-player:" in url) or ("roblox:" in url) or ("efaz-bootstrap" in url and "continue" in url) or ("efaz-bootstrap" in url and "new" in url):
            printDebugMessage(f"Running using Roblox URL: {url}")
            handler.openRoblox(forceQuit=(not (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True)), makeDupe=(fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True), debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True), startData=url)
            checkIfUpdateWasNeeded()
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
        handler.openRoblox(forceQuit=(not (fastFlagConfig.get("EFlagEnableDuplicationOfClients") == True)), debug=(fastFlagConfig.get("EFlagEnableDebugMode") == True))
        checkIfUpdateWasNeeded()
    os.system("exit")
    exit()