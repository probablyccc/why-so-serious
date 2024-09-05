# EfazRobloxBootstrap.spec

from PyInstaller.utils.hooks import collect_data_files
import os

# Paths and configurations
app_name = "EfazRobloxBootstrap"
icon_file = "AppIcon.icns"
plist = {
    "CFBundleExecutable": app_name,
    "CFBundleIdentifier": "dev.efaz.robloxbootstrap",
    "CFBundleURLTypes": [
        {
            "CFBundleTypeRole": "Viewer",
            "CFBundleURLName": "ReplicateRobloxPlayer",
            "CFBundleURLSchemes": ["roblox-player", "roblox", "efaz-bootstrap"],
        }
    ],
    "CFBundleName": app_name,
    "CFBundleVersion": "1.0.0",
    "LSMinimumSystemVersion": "10.9",
    "CFBundleIconFile": "AppIcon.icns",
    "CFBundleShortVersionString": "1.0.0",
    "CFBundleSignature": "????",
    "LSApplicationCategoryType": "public.app-category.utilities",
    "LSMultipleInstancesProhibited": False
}

block_cipher = None

a = Analysis(
    ["EfazRobloxBootstrap.py"],
    pathex=[],
    binaries=[],
    datas=collect_data_files("EfazRobloxBootstrap"),
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    argv_emulation=True,
    strip=False,
    upx=True,
    console=False,
    icon=os.path.join(os.getcwd(), icon_file),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=app_name,
    distpath='Apps',
)

# MacOS specific settings
app = BUNDLE(
    coll,
    name=app_name + ".app",
    icon=icon_file,
    bundle_identifier=plist["CFBundleIdentifier"],
    info_plist=plist,
    distpath='Apps',
    codesign_identity=None
)
