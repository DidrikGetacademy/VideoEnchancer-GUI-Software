# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files


a = Analysis(
    ['VideoEnchancer.py'],
    pathex=['C:\\Users\\didri\\Desktop\\LearnReflect VideoEnchancer'],
    binaries=[],
    datas=[(r"C:\Users\didri\Desktop\LearnReflect VideoEnchancer\Assets", "Assets"), (r"C:\Users\didri\Desktop\LearnReflect VideoEnchancer\AI-onnx", "AI-onnx")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='VideoEnchancer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon=r"C:\Users\didri\Desktop\LearnReflect VideoEnchancer\Assets\icon.ico",
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
