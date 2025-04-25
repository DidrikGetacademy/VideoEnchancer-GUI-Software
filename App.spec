
a = Analysis(
    [r'C:\Users\didri\Desktop\Programmering\VideoEnchancer program\App.py'],
    pathex=[r'C:\Users\didri\Desktop\Programmering\VideoEnchancer program'],
    binaries=[],
    datas=[
        (r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\local_model",'local_model'),
        (r'C:\Users\didri\Desktop\Programmering\VideoEnchancer program\BuildingFiles\dist\VideoEnchancer.exe', '.'),
        (r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\Assets", "Assets"),
        (r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\.env", "."), 

    ],
    hiddenimports=[
        'numpy.core',
        'threadpoolctl',
        'win32pdh',
        'yaml',
        'numpy.core',
        'numpy._typing',
        'numpy.lib',
        'numpy.ma',
        'numpy.linalg',
        'numpy.fft',
        'numpy.testing',
        'numpy.array_api',
        'numpy.core.arrayprint',
        'psutil',
        'brotli',
        'brotlicffi',
        'socks',
        'numpy.*',
    ],
    hookspath=[],
    hooksconfig={},
)

# PYZ creation
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# EXE creation
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LearnReflect_App',  # Output name of your GUI exe
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,  
    manifest=r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\BuildingFiles\ProgramApp.manifest",
    icon=r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\Assets\logo.ico",
)

# Collect everything
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,  # Include all data files and the VideoEnchancer.exe
    strip=False,
    upx=True,
    name='LearnReflect_App',  # Output directory name
    console=False,
    uac_admin=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
