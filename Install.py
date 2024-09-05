import shutil
import os
import platform
import json
import pip
import sys

def printMainMessage(mes):
    print(f"\033[38;5;255m{mes}\033[0m")

def printErrorMessage(mes):
    print(f"\033[38;5;196m{mes}\033[0m")

def printSuccessMessage(mes):
    print(f"\033[38;5;82m{mes}\033[0m")

def printWarnMessage(mes):
    print(f"\033[38;5;202m{mes}\033[0m")

def printDebugMessage(mes):
    print(f"\033[38;5;226m{mes}\033[0m")

def isYes(text):
    return text.lower() == "y" or text.lower() == "yes"

def isNo(text):
    return text.lower() == "n" or text.lower() == "no"

def isRequestClose(text):
    return text.lower() == "exit" or text.lower() == "exit()"

if __name__ == "__main__":
    main_os = platform.system()
    stored_main_app = {
        "Darwin": "/Applications/EfazRobloxBootstrap.app"
    }
    os.system("cls" if os.name == "nt" else "clear")
    printWarnMessage("-----------")
    printWarnMessage("Welcome to Efaz's Roblox Bootstrap Installer!")
    printWarnMessage("Made by Efaz from efaz.dev!")
    printWarnMessage("v1.0.0")
    printWarnMessage("-----------")
    printMainMessage("Determining System OS..")
    if main_os == "Darwin":
        found_platform = "Darwin"
    else:
        printErrorMessage("Installer is only available on macOS. Please run this script on macOS.")
        exit()

    printMainMessage("Installing Resources..")
    try:
        import requests
    except Exception as e:
        printMainMessage("Some modules are not installed. Do you want to install all the modules required now? (y/n)")
        if isYes(input("> ")) == True:
            pip.main(["install", "requests"])
            printSuccessMessage("Successfully installed modules!")
        else:
            printErrorMessage("Ending installation..")
            exit()
    overwrited = False
    if os.path.exists(stored_main_app[found_platform]):
        overwrited = True
    
    def install():
        printMainMessage("Installing to Applications Folder..")
        shutil.copytree(f"./Apps/EfazRobloxBootstrap.app", stored_main_app[found_platform], dirs_exist_ok=True)
        def ignore_files(dir, files):
            ignore_list = ["build", "Apps", "GenerateApp.py", "EfazRobloxBootstrap.spec", "FastFlagConfiguration.json", ".git"]
            return set(ignore_list) & set(files)
        printMainMessage("Preparing Contents..")
        if os.path.exists(stored_main_app[found_platform]):
            printMainMessage("Adding App Icon..")
            shutil.copy(f"AppIcon.icns", f"{stored_main_app[found_platform]}/Icon")
            printMainMessage("Copying Main Resources..")
            shutil.copytree(f"./", f"{stored_main_app[found_platform]}/Contents/Resources/", dirs_exist_ok=True, ignore=ignore_files)
            printMainMessage("Copying Configuration Files..")
            if not (os.path.exists(f"{stored_main_app[found_platform]}/Contents/Resources/FastFlagConfiguration.json")):
                with open(f"FastFlagConfiguration.json", "r") as f:
                    fastFlagConfig = json.loads(f.read())
                fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = os.getcwd()
                with open(f"{stored_main_app[found_platform]}/Contents/Resources/FastFlagConfiguration.json", "w") as f:
                    json.dump(fastFlagConfig, f, indent=4)
            else:
                with open(f"{stored_main_app[found_platform]}/Contents/Resources/FastFlagConfiguration.json", "r") as f:
                    fastFlagConfig = json.loads(f.read())
                fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = os.getcwd()
                with open(f"{stored_main_app[found_platform]}/Contents/Resources/FastFlagConfiguration.json", "w") as f:
                    json.dump(fastFlagConfig, f, indent=4)
            if overwrited == True:
                printSuccessMessage(f"Successfully updated Efaz's Roblox Bootstrap!")
            else:
                printSuccessMessage(f"Successfully installed Efaz's Roblox Bootstrap!")
        else:
            printErrorMessage("Something went wrong trying to find the application folder.")
    if len(sys.argv) > 1:
        if sys.argv[1] == "--install":
            install()
            exit()

    if overwrited == True:
        printWarnMessage("--- Updater ---")
        printMainMessage("Do you want to update Efaz's Roblox Bootstrap? (This will reupdate all files based on this Installation folder.) (y/n)")
    else:
        printWarnMessage("--- Installer ---")
        printMainMessage("Do you want to install Efaz's Roblox Bootstrap into your system? (This will add the app to your Applications folder.) (y/n)")
    res = input("> ")
    if isYes(res) == True:
        install()
        input("> ")
    exit()
else:
    printErrorMessage("The installer for the Efaz's Roblox Bootstrap macOS app is only a runable instance, not as a module.")