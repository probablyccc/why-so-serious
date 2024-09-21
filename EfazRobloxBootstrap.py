import sys
import subprocess
import json
import threading
import os
import platform
import time
import traceback

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

printWarnMessage("-----------")
printWarnMessage("Welcome to Efaz's Roblox Bootstrap Loader!")
printWarnMessage("Made by Efaz from efaz.dev!")
printWarnMessage("v1.1.5")
printWarnMessage("-----------")
printMainMessage("Determining System OS..")
main_os = platform.system()
direct_run = False

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
    args = sys.argv
    if main_os == "Darwin":
        execute_command = ""
        filtered_args = ""
        loaded_json = True
        use_shell = False

        def displayMacOSNotification(title, message):
            import objc
            NSUserNotification = objc.lookUpClass("NSUserNotification")
            NSUserNotificationCenter = objc.lookUpClass("NSUserNotificationCenter")

            notification = NSUserNotification.alloc().init()
            notification.setTitle_(title)
            notification.setInformativeText_(message)
            center = NSUserNotificationCenter.defaultUserNotificationCenter()
            center.deliverNotification_(notification)

        if os.path.exists("/Applications/EfazRobloxBootstrap.app/Contents/Resources/FastFlagConfiguration.json"):
            with open("/Applications/EfazRobloxBootstrap.app/Contents/Resources/FastFlagConfiguration.json", "r") as f:
                try:
                    fastFlagConfig = json.loads(f.read())
                except Exception as e:
                    loaded_json = False
        else:
            with open("FastFlagConfiguration.json", "r") as f:
                try:
                    fastFlagConfig = json.loads(f.read())
                except Exception as e:
                    loaded_json = False

        if pip().pythonInstalled() == False: pip().pythonInstall()

        if len(args) > 1:
            filtered_args = args[1]
            if (("roblox-player:" in filtered_args) or ("roblox:" in filtered_args)) and not (loaded_json == True and fastFlagConfig.get("EFlagEnableDebugMode") == True):
                use_shell = True
                if fastFlagConfig.get("EFlagEnableDebugMode"): printDebugMessage("Moved command execution to file args to prevent user from showing the command with private info.")
                if os.path.exists("/Applications/EfazRobloxBootstrap.app/Contents/Resources/"):
                    with open("/Applications/EfazRobloxBootstrap.app/Contents/Resources/URLSchemeExchange", "w") as f:
                        f.write(filtered_args)
                else:
                    with open("URLSchemeExchange", "w") as f:
                        f.write(filtered_args)
        execute_command = f'cd /Applications/EfazRobloxBootstrap.app/Contents/Resources/ && python3 Main.py && exit'
        printSuccessMessage(f"Generated Python Command: {execute_command}")

        if direct_run == False:
            applescript = f'''
            tell application "Terminal"
                set command to "{execute_command}"
                set py_window to do script command
                activate
                repeat
                    delay 1
                    try
                        if (busy of py_window) is false then
                            exit repeat
                        end if
                    on error errMsg number errNum
                        exit repeat
                    end try
                end repeat
                try
                    close py_window
                on error
                    set canCloseWindows to (every window whose processes = {"{}"})
                    repeat with windowToClose in canCloseWindows
                        close windowToClose
                    end repeat
                end try
            end tell
            '''

            try:
                ended = False
                printMainMessage(f"Running Python3 Command..")
                def awake():
                    seconds = 0
                    while True:
                        if ended == True:
                            break
                        if os.path.exists("/Applications/EfazRobloxBootstrap.app/Contents/Resources/MacOSNotification"):
                            with open("/Applications/EfazRobloxBootstrap.app/Contents/Resources/MacOSNotification", "r") as f:
                                try:
                                    notification = json.loads(f.read())
                                except Exception as e:
                                    printDebugMessage(str(e))
                                    notification = {"title": "Something went wrong.", "message": "An unexpected error occurred while loading this notification."}
                            os.remove("/Applications/EfazRobloxBootstrap.app/Contents/Resources/MacOSNotification")
                            if notification.get("title") and notification.get("message"):
                                displayMacOSNotification(notification["title"], notification["message"])
                            
                        seconds += 1
                        printMainMessage(f"Waken for {seconds} seconds")
                        time.sleep(1)
                threading.Thread(target=awake).start() 
                result = subprocess.run(args=["osascript", "-e", applescript], check=True, capture_output=True)
                printSuccessMessage(f"Command Run Success: {result.returncode}")
                ended = True
            except Exception as e:
                traceback.print_exc()
                traceback_err_str = traceback.format_exc()
                printErrorMessage(f"An error occurred: {traceback_err_str}")
        else:
            try:
                ended = False
                printMainMessage(f"Running Python3 Command..")
                def awake():
                    seconds = 0
                    while True:
                        if ended == True:
                            break
                        if os.path.exists("/Applications/EfazRobloxBootstrap.app/Contents/Resources/MacOSNotification"):
                            with open("/Applications/EfazRobloxBootstrap.app/Contents/Resources/MacOSNotification", "r") as f:
                                try:
                                    notification = json.loads(f.read())
                                except Exception as e:
                                    printDebugMessage(str(e))
                                    notification = {"title": "Something went wrong.", "message": "An unexpected error occurred while loading this notification."}
                            if notification.get("title") and notification.get("message"):
                                displayMacOSNotification(notification["title"], notification["message"])
                            if os.path.exists("/Applications/EfazRobloxBootstrap.app/Contents/Resources/MacOSNotification"):
                                try: 
                                    os.remove("/Applications/EfazRobloxBootstrap.app/Contents/Resources/MacOSNotification")
                                except Exception as e: 
                                    printErrorMessage(str(e))
                            
                        seconds += 1
                        printMainMessage(f"Waken for {seconds} seconds")
                        time.sleep(1)
                def main_process():
                    try:
                        global ended
                        if not (filtered_args == "" or filtered_args == None):
                            result = subprocess.run(["python3", "Main.py", filtered_args], check=True, capture_output=True, shell=True)
                        else:
                            result = subprocess.run(["python3", "Main.py"], check=True, capture_output=True)
                        printSuccessMessage(f"Command Run Success: {result.returncode}")
                        ended = True
                        sys.exit(0)
                    except Exception as e:
                        printErrorMessage(str(e))
                threading.Thread(target=awake).start()
                main_process()
            except Exception as e:
                printErrorMessage(f"An error occurred: {str(e)}")
    elif main_os == "Windows":
        filtered_args = ""
        loaded_json = True
        
        if os.path.exists(os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap", "Main.py")):
            os.system("title Efaz's Roblox Bootstrap")
            
            with open(os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap", "FastFlagConfiguration.json"), "r") as f:
                try:
                    fastFlagConfig = json.loads(f.read())
                except Exception as e:
                    loaded_json = False

            if len(args) > 1:
                cou = 0
                filtered_args = ""
                for i in args:
                    if cou > 0:
                        filtered_args = f"{i} "
                    cou += 1

            if pip().pythonInstalled() == False: pip().pythonInstall()
            try:
                if filtered_args == "":
                    result = subprocess.run(["py", os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap", "Main.py")], shell=True, cwd=os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap"))
                else:
                    result = subprocess.run(["py", os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap", "Main.py"), filtered_args], shell=True, cwd=os.path.join(f"{os.getenv('LOCALAPPDATA')}", "EfazRobloxBootstrap"))
                printSuccessMessage(f"App Run Success: {result.returncode}")
                sys.exit(0)
            except Exception as e:
                printErrorMessage(f"An error occurred: {str(e)}")
        else:
            printMainMessage("Please install the progam using the Install.py command!!")
            input("> ")