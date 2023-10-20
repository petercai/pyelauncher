# -*- mode: python ; coding: utf-8 -*-

options = [
    ('v', None, 'OPTION'),
    ('W ignore', None, 'OPTION'),
]

a = Analysis(
    ['launcherApp.py'],
    pathex=[],
    binaries=[],
    datas=[('config/elauncher.xml', 'config')],
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
    options,  # <-- the options list, passed to EXE
    [],
    exclude_binaries=True,
    name='peppermintLauncher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['peppermint.jpg'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='peppermintLauncher',
)
