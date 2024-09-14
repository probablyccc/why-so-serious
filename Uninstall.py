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
        "Darwin": ["/Applications/EfazRobloxBootstrap.app", "/Applications/EfazRobloxBootstrapLoader.app"],
        "Windows": [f"{os.getenv('LOCALAPPDATA')}\\EfazRobloxBootstrap", f"{os.getenv('LOCALAPPDATA')}\\EfazRobloxBootstrap\\EfazRobloxBootstrap.exe"]
    }
    handler = RobloxFastFlagsInstaller.Main()

    os.system("cls" if os.name == "nt" else "clear")
    printWarnMessage("-----------")
    printWarnMessage("Welcome to Efaz's Roblox Bootstrap Installer!")
    printWarnMessage("Made by Efaz from efaz.dev!")
    printWarnMessage("v1.1.0")
    printWarnMessage("-----------")
    printMainMessage("Determining System OS..")
    if main_os == "Darwin":
        found_platform = "Darwin"
    elif main_os == "Windows":
        found_platform = "Windows"
    else:
        printErrorMessage("Installer is only available on macOS or Windows.")
        exit()
    printWarnMessage("--- Uninstaller ---")
    printMainMessage("Are you sure you want to uninstall Efaz's Roblox Bootstrap from your system? (This will remove the app and reinstall Roblox.) (y/n)")
    if isYes(input("> ")) == True:
        if main_os == "Darwin":
            if os.path.exists(stored_main_app[found_platform][0]):
                printMainMessage("Removing from Applications Folder (1)..")
                shutil.rmtree(stored_main_app[found_platform][0])
            if os.path.exists(stored_main_app[found_platform][1]):
                printMainMessage("Removing from Applications Folder (2)..")
                shutil.rmtree(stored_main_app[found_platform][1])
        elif main_os == "Windows":
            if os.path.exists(stored_main_app[found_platform][0]):
                printMainMessage("Removing App Folder..")
                shutil.rmtree(stored_main_app[found_platform][0])
            printMainMessage("Resetting URL Schemes")
            import winreg
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

            set_url_scheme("efaz-bootstrap", "")
            cur = handler.getCurrentClientVersion()
            if cur:
                if cur["success"] == True:
                    set_url_scheme("roblox-player", f"{os.getenv('LOCALAPPDATA')}\\Roblox\\Versions\\{cur['version']}\\RobloxPlayerBeta.exe")
                    set_url_scheme("roblox", f"{os.getenv('LOCALAPPDATA')}\\Roblox\\Versions\\{cur['version']}\\RobloxPlayerBeta.exe")

            app_key = r"Software\EfazRobloxBootstrap"
            uninstall_key = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\EfazRobloxBootstrap"

            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, app_key, 0, winreg.KEY_WRITE) as key:
                    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, app_key)
            except FileNotFoundError:
                printErrorMessage(f'Registry key {app_key} not found.')
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, uninstall_key, 0, winreg.KEY_WRITE) as key:
                    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, uninstall_key)
            except FileNotFoundError:
                printErrorMessage(f'Registry key {uninstall_key} not found.')
        printMainMessage("Preparing to reinstall Roblox..")
        handler.installRoblox(True, True)
        printSuccessMessage("Successfully reinstalled Roblox!")
        printSuccessMessage("Successfully uninstalled Efaz's Roblox Bootstrap!")
        input("> ")
    exit()
else:
    printErrorMessage("The installer for the Efaz's Roblox Bootstrap app is only a runable instance, not as a module.")