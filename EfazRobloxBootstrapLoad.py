import sys
import os
import subprocess
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
printWarnMessage("v1.1.5")
printWarnMessage("-----------")
printMainMessage("Determining System OS..")
main_os = platform.system()
direct_run = False

if __name__ == "__main__":
    args = sys.argv
    if main_os == "Darwin":
        if os.path.exists("/Applications/EfazRobloxBootstrap.app/"):
            if len(args) == 1:
                printMainMessage("Redirected to loader! 0/1")
                subprocess.run(["open", "-n", "-a", "/Applications/EfazRobloxBootstrap.app/Contents/MacOS/EfazRobloxBootstrap"], cwd="/Applications/EfazRobloxBootstrap.app/Contents/Resources/", stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                sys.exit(0)
            elif len(args) > 1:
                printMainMessage("Redirected to loader! 0/1")
                with open("/Applications/EfazRobloxBootstrap.app/Contents/Resources/URLSchemeExchange", "w") as f:
                    f.write(args[1])
                subprocess.run(["open", "-n", "-a", "/Applications/EfazRobloxBootstrap.app/Contents/MacOS/EfazRobloxBootstrap"], cwd="/Applications/EfazRobloxBootstrap.app/Contents/Resources/", stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                sys.exit(0)