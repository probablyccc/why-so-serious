import shutil
import os
import platform
import json
import sys

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
        import requests
        import subprocess
        import tempfile

        ma_os = platform.system()
        if ma_os == "Darwin":
            url = "https://www.python.org/ftp/python/3.12.5/python-3.12.5-macos11.pkg"
            response = requests.get(url)
            
            if response.status_code == 200:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pkg") as pkg_file:
                    pkg_file.write(response.content)
                    pkg_file_path = pkg_file.name
                subprocess.run(["open", pkg_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                print(f"Python installer has been executed: {pkg_file_path}")
            else:
                print("Failed to download Python installer.")
        elif ma_os == "Windows":
            url = "https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe"
            response = requests.get(url)
            
            if response.status_code == 200:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".exe") as exe_file:
                    exe_file.write(response.content)
                    exe_file_path = exe_file.name
                subprocess.run([exe_file_path], check=True)
                print(f"Python installer has been executed: {exe_file_path}")
            else:
                print("Failed to download Python installer.")

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
        "Windows": [os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap"), os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap", "EfazRobloxBootstrap.exe")]
    }
    instant_install = False

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
        printErrorMessage("This installer is only available on macOS or Windows.")
        exit()

    printMainMessage("Installing Resources..")
    try:
        import requests
        import plyer
        import pypresence
        if main_os == "Windows":
            import win32com.client
    except Exception as e:
        printMainMessage("Some modules are not installed and may be needed for some features. Do you want to install all the modules needed now? (y/n)")
        if instant_install == True or isYes(input("> ")) == True:
            pip().install(["requests"])
            pip().install(["plyer"])
            pip().install(["pypresence"])
            if main_os == "Windows":
                pip().install(["pywin32"])
            printSuccessMessage("Successfully installed modules!")
        else:
            printErrorMessage("Ending installation..")
            exit()
    overwrited = False
    if os.path.exists(stored_main_app[found_platform][0]) and os.path.exists(stored_main_app[found_platform][1]):
        overwrited = True
    
    def install():
        if main_os == "Darwin":
            printMainMessage("Installing to Applications Folder..")
            shutil.copytree(f"./Apps/EfazRobloxBootstrap.app", stored_main_app[found_platform][0], dirs_exist_ok=True)
            shutil.copytree(f"./Apps/EfazRobloxBootstrapLoad.app", stored_main_app[found_platform][1], dirs_exist_ok=True)
            def ignore_files(dir, files):
                ignore_list = ["build", "Apps", "GenerateApp.py", "EfazRobloxBootstrap.spec", "FastFlagConfiguration.json", ".git"]
                return set(ignore_list) & set(files)
            printMainMessage("Preparing Contents..")
            if os.path.exists(stored_main_app[found_platform][0]):
                printMainMessage("Adding App Icon..")
                shutil.copy(f"AppIcon.icns", f"{stored_main_app[found_platform][0]}/Icon")
                printMainMessage("Copying Main Resources..")
                shutil.copytree(f"./", f"{stored_main_app[found_platform][0]}/Contents/Resources/", dirs_exist_ok=True, ignore=ignore_files)
                printMainMessage("Copying Configuration Files..")
                if not (os.path.exists(f"{stored_main_app[found_platform][0]}/Contents/Resources/FastFlagConfiguration.json")):
                    with open(f"FastFlagConfiguration.json", "r") as f:
                        fastFlagConfig = json.loads(f.read())
                    fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = os.getcwd()
                    with open(f"{stored_main_app[found_platform][0]}/Contents/Resources/FastFlagConfiguration.json", "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                else:
                    with open(f"{stored_main_app[found_platform][0]}/Contents/Resources/FastFlagConfiguration.json", "r") as f:
                        fastFlagConfig = json.loads(f.read())
                    fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = os.getcwd()
                    with open(f"{stored_main_app[found_platform][0]}/Contents/Resources/FastFlagConfiguration.json", "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                if overwrited == True:
                    printSuccessMessage(f"Successfully updated Efaz's Roblox Bootstrap!")
                else:
                    printSuccessMessage(f"Successfully installed Efaz's Roblox Bootstrap!")
            else:
                printErrorMessage("Something went wrong trying to find the application folder.")
        elif main_os == "Windows":
            printMainMessage("Creating paths..")
            os.makedirs(stored_main_app[found_platform][0], exist_ok=True)
            disabled_url_schemes = False

            printMainMessage("Installing EXE File..")
            shutil.copy(os.path.join(os.curdir, "Apps", "EfazRobloxBootstrap", "EfazRobloxBootstrap.exe"), stored_main_app[found_platform][1])
            shutil.copytree(os.path.join(os.curdir, "Apps", "EfazRobloxBootstrap", "_internal"), os.path.join(stored_main_app[found_platform][0], "_internal"), dirs_exist_ok=True)

            import winreg
            if instant_install == False:
                printMainMessage("Would you like to install URL Schemes?")
                a = input("> ")
                if not (a.lower() == "n"):
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
                    set_url_scheme("efaz-bootstrap", stored_main_app[found_platform][1])
                    set_url_scheme("roblox-player", stored_main_app[found_platform][1])
                    set_url_scheme("roblox", stored_main_app[found_platform][1])
                else:
                    disabled_url_schemes = True

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
            create_shortcut(stored_main_app[found_platform][1], os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'), 'EfazRobloxBootstrap.lnk'))
            create_shortcut(stored_main_app[found_platform][1], os.path.join(os.path.join(os.path.join(os.environ['APPDATA']), 'Microsoft', 'Windows', 'Start Menu', 'Programs'), 'EfazRobloxBootstrap.lnk'))

            printMainMessage("Calling Windows to mark program as installed.")
            app_key = "Software\\EfazRobloxBootstrap"
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, app_key) as key:
                winreg.SetValueEx(key, "InstallPath", 0, winreg.REG_SZ, stored_main_app[found_platform][0])
                winreg.SetValueEx(key, "Installed", 0, winreg.REG_DWORD, 1)

            registry_path = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\EfazRobloxBootstrap"
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, registry_path) as key:
                winreg.SetValueEx(key, "UninstallString", 0, winreg.REG_SZ, f"py {os.path.join(stored_main_app[found_platform][0], "Uninstall.py")}")
                winreg.SetValueEx(key, "DisplayName", 0, winreg.REG_SZ, "Efaz's Roblox Bootstrap")
                winreg.SetValueEx(key, "DisplayVersion", 0, winreg.REG_SZ, "1.1.0")
                winreg.SetValueEx(key, "DisplayIcon", 0, winreg.REG_SZ, os.path.join(stored_main_app[found_platform][0], "AppIcon.ico"))

            printMainMessage("Copying App Resources..")
            def ignore_files(dir, files):
                ignore_list = ["build", "Apps", "GenerateApp.py", "EfazRobloxBootstrap.spec", "_internal", "FastFlagConfiguration.json", ".git"]
                return set(ignore_list) & set(files)
            if os.path.exists(stored_main_app[found_platform][1]):
                shutil.copytree(os.curdir, stored_main_app[found_platform][0], dirs_exist_ok=True, ignore=ignore_files)
                printMainMessage("Copying Configuration Files..")
                if not (os.path.exists(os.path.join(f"{stored_main_app[found_platform][0]}", "FastFlagConfiguration.json"))):
                    with open(f"FastFlagConfiguration.json", "r") as f:
                        fastFlagConfig = json.loads(f.read())
                    if disabled_url_schemes == True:
                        fastFlagConfig["EFlagDisableURLSchemeInstall"] = True
                    else:
                        fastFlagConfig["EFlagDisableURLSchemeInstall"] = False
                    fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = os.getcwd()
                    with open(os.path.join(f"{stored_main_app[found_platform][0]}", "FastFlagConfiguration.json"), "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                else:
                    with open(os.path.join(f"{stored_main_app[found_platform][0]}", "FastFlagConfiguration.json"), "r") as f:
                        fastFlagConfig = json.loads(f.read())
                    if disabled_url_schemes == True:
                        fastFlagConfig["EFlagDisableURLSchemeInstall"] = True
                    else:
                        fastFlagConfig["EFlagDisableURLSchemeInstall"] = False
                    fastFlagConfig["EFlagEfazRobloxBootStrapSyncDir"] = os.getcwd()
                    with open(os.path.join(f"{stored_main_app[found_platform][0]}", "FastFlagConfiguration.json"), "w") as f:
                        json.dump(fastFlagConfig, f, indent=4)
                if overwrited == True:
                    printSuccessMessage(f"Successfully updated Efaz's Roblox Bootstrap!")
                else:
                    printSuccessMessage(f"Successfully installed Efaz's Roblox Bootstrap!")
            else:
                printErrorMessage("Something went wrong trying to find the installation folder.")

    if len(sys.argv) > 1:
        if sys.argv[1] == "--install":
            instant_install = True
            printWarnMessage("--- Installer ---")
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
    printErrorMessage("The installer for the Efaz's Roblox Bootstrap app is only a runable instance, not as a module.")