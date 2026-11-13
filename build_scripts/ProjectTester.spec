# -*- mode: python ; coding: utf-8 -*-

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(SPECPATH)))
import build_meta

# Version resource is generated from app_info.py (single source of truth)
VERSION_FILE = build_meta.write_windows_version_file(
    os.path.join(SPECPATH, '_generated_version_info.txt'))

block_cipher = None

a = Analysis(
    ['../tester.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('../assets/icon.png', 'assets'),
        ('../assets/copy.png', 'assets'),
        ('../data', 'data'),
        ('../config.json', '.'),
        ('../predefined_inputs.json', '.'),
        ('../feedback_template.txt', '.'),
    ],
    hiddenimports=[
        'pygments',
        'pygments.lexers',
        'pygments.lexers.python',
        'pygments.token',
        'watchdog',
        'watchdog.observers',
        'watchdog.events',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'PIL',
        'pytest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Project-Tester',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version=VERSION_FILE,
    icon='../assets/icon.png',
    uac_admin=False,  # Don't require admin rights
    uac_uiaccess=False,
)
