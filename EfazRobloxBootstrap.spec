from PyInstaller.utils.hooks import collect_data_files
import os

app_name = "EfazRobloxBootstrap"
icon_file = "AppIcon.icns"
plist1 = {
    "CFBundleExecutable": "EfazRobloxBootstrap",
    "CFBundleIdentifier": "dev.efaz.robloxbootstrap",
    "CFBundleURLTypes": [],
    "CFBundleName": "EfazRobloxBootstrap",
    "CFBundleVersion": "1.0.0",
    "LSMinimumSystemVersion": "10.9",
    "CFBundleIconFile": "AppIcon.icns",
    "CFBundleShortVersionString": "1.0.0",
    "CFBundleSignature": "????",
    "LSApplicationCategoryType": "public.app-category.utilities",
    "LSMultipleInstancesProhibited": False,
    "NSAppSleepDisabled": True,
}
plist2 = {
    "CFBundleExecutable": "EfazRobloxBootstrapLoad",
    "CFBundleIdentifier": "dev.efaz.robloxbootstrap",
    "CFBundleURLTypes": [
        {
            "CFBundleTypeRole": "Viewer",
            "CFBundleURLName": "ReplicateRobloxPlayer",
            "CFBundleURLSchemes": ["roblox-player", "roblox", "efaz-bootstrap"],
        }
    ],
    "CFBundleName": "EfazRobloxBootstrapLoad",
    "CFBundleVersion": "1.0.0",
    "LSMinimumSystemVersion": "10.9",
    "CFBundleIconFile": "AppIcon.icns",
    "CFBundleShortVersionString": "1.0.0",
    "CFBundleSignature": "????",
    "LSApplicationCategoryType": "public.app-category.utilities",
    "LSMultipleInstancesProhibited": False,
    "NSAppSleepDisabled": True,
}

block_cipher = None

a = Analysis(
    ["EfazRobloxBootstrap.py", "EfazRobloxBootstrapLoad.py"],
    pathex=[],
    binaries=[],
    datas=collect_data_files("EfazRobloxBootstrap"),
    hiddenimports=["requests", "pyobjc", "subprocess"],
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

exe1 = EXE(
    pyz,
    [a.scripts[1]],
    exclude_binaries=True,
    name="EfazRobloxBootstrap",
    debug=False,
    bootloader_ignore_signals=False,
    argv_emulation=True,
    strip=False,
    console=False,
    upx=True,
    icon=os.path.join(os.getcwd(), icon_file),
)
exe2 = EXE(
    pyz,
    [a.scripts[2]],
    exclude_binaries=True,
    name="EfazRobloxBootstrapLoad",
    debug=False,
    bootloader_ignore_signals=False,
    argv_emulation=True,
    strip=False,
    upx=True,
    console=False,
    icon=os.path.join(os.getcwd(), icon_file),
)

coll1 = COLLECT(
    exe1,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=app_name,
    distpath='Apps',
)
coll2 = COLLECT(
    exe2,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="EfazRobloxBootstrapLoad",
    distpath='Apps',
)

app1 = BUNDLE(
    coll1,
    name=app_name + ".app",
    icon=icon_file,
    bundle_identifier=plist1["CFBundleIdentifier"],
    info_plist=plist1,
    distpath='Apps',
    codesign_identity=None
)
app2 = BUNDLE(
    coll2,
    name="EfazRobloxBootstrapLoad.app",
    icon=icon_file,
    bundle_identifier=plist2["CFBundleIdentifier"],
    info_plist=plist2,
    distpath='Apps',
    codesign_identity=None
)