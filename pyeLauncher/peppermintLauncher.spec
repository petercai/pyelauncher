# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['launcherApp.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PeppermintLauncher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['peppermint.jpg'],
)

import os
import shutil
import zipfile


dest_path = os.path.join(DISTPATH,'config')
os.makedirs(dest_path, exist_ok=True)
shutil.copyfile(os.path.join('config','elauncher.xml'), os.path.join(dest_path,'elauncher.xml'))

import os

def zip_folder(folder_path, zip_filename, root_folder):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, folder_path)
                zip_path = os.path.join(root_folder, rel_path)
                zipf.write(file_path, zip_path)



zip_file_name = 'PeppermintLauncher-win-x64-portable.zip'

# Create the zip file
zip_folder(DISTPATH, zip_file_name, 'PeppermintLauncher')
