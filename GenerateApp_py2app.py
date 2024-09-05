# Do not use this script if you want to get a speedy experience, only pyinstaller

from setuptools import setup

APP = ["EfazRobloxBootstrap.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": [],
    "iconfile": "AppIcon.icns",
    "plist": {
        "CFBundleExecutable": "EfazRobloxBootstrap",
        "CFBundleIdentifier": "dev.efaz.robloxbootstrap",
        "CFBundleURLTypes": [
            {
                "CFBundleTypeRole": "Viewer",
                "CFBundleURLName": "ReplicateRobloxPlayer",
                "CFBundleURLSchemes": ["roblox-player", "roblox", "efaz-bootstrap"],
            }
        ],
        "CFBundleName": "EfazRobloxBootstrap",
        "CFBundleVersion": "1.0.0",
        "LSMinimumSystemVersion": "10.9",
        "CFBundleIconFile": "AppIcon.icns",
        "CFBundleSignature": "????",
        "LSApplicationCategoryType": "public.app-category.utilities",
        "LSMultipleInstancesProhibited": False
    },
}

setup(app=APP, data_files=DATA_FILES, options={"py2app": OPTIONS}, setup_requires=["py2app"])