#
# Hello there!
# Welcome to the insides of ModScript.py!
# This can allow you to run functions for when events from RobloxFastFlagsInstaller.py are ran!
# If you're a python developer, you may be able to get started here!
# [Only one script can be run but you can make a script that could handle more scripts if you want.]
# 

# Python Modules
import platform
import json
import os
import time

# API Functions
def getFastFlagConfiguration():
    with open("FastFlagConfiguration.json") as f:
        try:
            return json.load(f)
        except Exception as e:
            printErrorMessage("Unable to read configuration. Script may be running outside of system.")
            return None
def getPlatform():
    s = platform.system()
    if s == "Windows":
        return "Windows"
    elif s == "Darwin":
        return "macOS"
    else:
        return "Linux"
def displayNotification(title, message):
    if getPlatform() == "macOS":
        import objc
        NSUserNotification = objc.lookUpClass("NSUserNotification")
        NSUserNotificationCenter = objc.lookUpClass("NSUserNotificationCenter")
        notification = NSUserNotification.alloc().init()
        notification.setTitle_(title)
        notification.setInformativeText_(message)
        center = NSUserNotificationCenter.defaultUserNotificationCenter()
        center.deliverNotification_(notification)
    elif getPlatform() == "Windows":
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
    
# API Variables
fastFlagConfig = getFastFlagConfiguration()
    
# Printing Functions
def printMainMessage(mes): # White System Console Text
    print(f"\033[38;5;255m[MOD SCRIPT]: {mes}\033[0m")
def printErrorMessage(mes): # Error Colored Console Text
    print(f"\033[38;5;196m[MOD SCRIPT]: {mes}\033[0m")
def printSuccessMessage(mes): # Success Colored Console Text
    print(f"\033[38;5;82m[MOD SCRIPT]: {mes}\033[0m")
def printWarnMessage(mes): # Orange Colored Console Text
    print(f"\033[38;5;202m[MOD SCRIPT]: {mes}\033[0m")
def printYellowMessage(mes): # Yellow Colored Console Text
    print(f"\033[38;5;226m[MOD SCRIPT]: {mes}\033[0m")
def printDebugMessage(mes): # Debug Console Text
    if fastFlagConfig.get("EFlagEnableDebugMode") == True:
        print(f"\033[38;5;226m{mes}\033[0m")

# Main Handler
def onRobloxAppStart(data):
    printMainMessage("Hello there!")
    printMainMessage("This is a template mod script here!")
    printMainMessage("This is ran when Roblox opened earlier.")
    printMainMessage("If you know python, try editing ModScript.py and installing through Install.py!")

def onRobloxCrash(data):
    printMainMessage("Oof! Roblox crashed!")

def onBloxstrapSDK(data):
    printMainMessage("Bloxstrap SDK requested!")

def onRobloxPassedUpdate(data):
    printSuccessMessage("Woo hoo! Roblox passed the update check!")

def onGameDisconnected(data):
    printErrorMessage("The template script detected the game disconnect. :(")

def onGameJoined(data):
    printSuccessMessage("Woo hoo! The template script detected you joined a game!")