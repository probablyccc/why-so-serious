import os
import platform
import shutil
import RobloxFastFlagsInstaller

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
    handler = RobloxFastFlagsInstaller.Main()

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
    printWarnMessage("--- Uninstaller ---")
    printMainMessage("Are you sure you want to uninstall Efaz's Roblox Bootstrap from your system? (This will remove the app and reinstall Roblox.) (y/n)")
    if isYes(input("> ")) == True:
        if os.path.exists(stored_main_app[found_platform]):
            printMainMessage("Removing from Applications Folder..")
            shutil.rmtree(f"/Applications/EfazRobloxBootstrap.app")
        printMainMessage("Preparing to reinstall Roblox..")
        handler.updateRoblox(True, True)
        printSuccessMessage("Successfully reinstalled Roblox!")
    exit()
else:
    printErrorMessage("The installer for the Efaz's Roblox Bootstrap macOS app is only a runable instance, not as a module.")