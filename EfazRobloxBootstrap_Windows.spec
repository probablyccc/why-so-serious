from PyInstaller.utils.hooks import collect_data_files
import os

app_name = "EfazRobloxBootstrap"
icon_file = "AppIcon.ico"
script_path = "EfazRobloxBootstrap.py"
block_cipher = None

a = Analysis(
    [script_path],
    pathex=[],
    binaries=[],
    datas=collect_data_files("EfazRobloxBootstrap"),
    hiddenimports=["subprocess"],
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
    [a.scripts[1]],
    exclude_binaries=True,
    name="EfazRobloxBootstrap",
    debug=False,
    bootloader_ignore_signals=False,
    argv_emulation=True,
    strip=False,
    console=True,
    upx=True,
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
    distpath='dist',
)