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
app = BUNDLE(
    exe,
    name='PeppermintLauncher.app',
    icon='peppermint.jpg',
    bundle_identifier=None,
)

import os
import shutil


dest_path = os.path.join(DISTPATH,'config')
os.makedirs(dest_path, exist_ok=True)
shutil.copyfile(os.path.join('config','elauncher.xml'), os.path.join(dest_path,'elauncher.xml'))
