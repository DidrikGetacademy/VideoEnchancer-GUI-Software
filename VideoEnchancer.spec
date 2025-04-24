# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_all, collect_dynamic_libs, collect_data_files

# Logging setup (optional)
log_file = "datas_check_log.txt"
with open(log_file, "w") as log:
    log.write("=== Checking datas entries ===\n")

# Define your datas
raw_datas = [
    (r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\AI-onnx", "AI-onnx"), 
    (r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\.env", "."), #Env 
    (r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\Assets", "Assets"),
    (r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\vocal_isolation\app.py", "vocal_isolation") 
]

# Validate existence
datas = []
for src, dest in raw_datas:
    exists = os.path.exists(src)
    with open(log_file, "a") as log:
        log.write(f"{'✔' if exists else '❌'} {src} → {dest}\n")
    if exists:
        datas.append((src, dest))
    else:
        print(f"[WARNING] Missing data source: {src}")

# Add dependencies
binaries  = collect_dynamic_libs('torch')
binaries += collect_dynamic_libs('numba')

hiddenimports = ['natsort','moviepy.editor','moviepy.audio.io.AudioFileClip','moviepy.video.io.VideoFileClip','psutil','onnxruntime']
tmp_ret = collect_all('numba')
hiddenimports += tmp_ret[2]

a = Analysis(
    ['VideoEnchancer.py'],
    pathex=[r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program"],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    icon=r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\Assets\LearnReflect.ico",
    uac_admin=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    manifest=r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\BuildingFiles\ProgramVideoEnancer.manifest",
)
