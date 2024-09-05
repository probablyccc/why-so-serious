import sys
import subprocess
import json
import platform

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
printWarnMessage("v1.0.0")
printWarnMessage("-----------")
printMainMessage("Determining System OS..")
main_os = platform.system()
direct_run = False

if __name__ == "__main__":
    args = sys.argv
    if main_os == "Darwin":
        command = ""
        hide_command = "do script"
        extra = ""
        loadedJSON = True

        with open("/Applications/EfazRobloxBootstrap.app/Contents/Resources/FastFlagConfiguration.json", "r") as f:
            try:
                fastFlagConfig = json.loads(f.read())
            except Exception as e:
                loadedJSON = False

        if len(args) > 1:
            if (("roblox-player:" in args[1]) or ("roblox:" in args[1])) and not (loadedJSON == True and fastFlagConfig.get("EFlagEnableDebugMode") == True):
                hide_command = "do shell script"
            extra = args[1]
            command = f"cd /Applications/EfazRobloxBootstrap.app/Contents/Resources/ && python3 Main.py {args[1]} && exit"
            printSuccessMessage(f"Generated Python Command!")
        else:
            command = 'cd /Applications/EfazRobloxBootstrap.app/Contents/Resources/ && python3 Main.py && exit'
            printSuccessMessage(f"Generated Python Command: {command}")

        if direct_run == False:
            applescript = f'''
            tell application "Terminal"
                set command to "{command}"
                set py_window to {hide_command} command
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
            if hide_command == "do shell script":
                applescript = f'''
                set command to "{command}"
                try
                    do shell script command
                on error
                    set canCloseWindows to (every window whose processes = {"{}"})
                    repeat with windowToClose in canCloseWindows
                        close windowToClose
                    end repeat
                end try
                '''
                if fastFlagConfig.get("EFlagEnableDebugMode"): printDebugMessage("Moved command execution to shell to prevent user from showing the command with private info.")

            try:
                printMainMessage(f"Running Python3 Command..")
                result = subprocess.run(['osascript', '-e', applescript], check=True, text=True, capture_output=True)
                printSuccessMessage(f"Command Run Success: {result.stdout}")
            except Exception as e:
                printErrorMessage(f"An error occurred: {str(e)}")
        else:
            try:
                printMainMessage(f"Running Python3 Command..")
                result = subprocess.run(["python3", "Main.py", extra], check=True, text=True, capture_output=True)
                printSuccessMessage(f"Command Run Success: {result.stdout}")
            except Exception as e:
                printErrorMessage(f"An error occurred: {str(e)}")
    elif main_os == "Windows":
        extra = ""
        loadedJSON = True
        
        with open("FastFlagConfiguration.json", "r") as f:
            try:
                fastFlagConfig = json.loads(f.read())
            except Exception as e:
                loadedJSON = False

        if len(args) > 1:
            extra = args[1]
            printErrorMessage("[WARNING]: DO NOT EVER SHOW ANYONE THIS INFORMATION SINCE IT MAY GIVE ACCESS TO YOUR ROBLOX ACCOUNT")
            printSuccessMessage(f"Generated Python Command!")
        else:
            printSuccessMessage(f"Generated Python Command: py Main.py && exit")
        try:
            printMainMessage(f"Running Python3 Command..")
            result = subprocess.run(["py", "Main.py", extra], check=True, text=True, capture_output=True)
            printSuccessMessage(f"Command Run Success: {result.stdout}")
        except Exception as e:
            printErrorMessage(f"An error occurred: {str(e)}")