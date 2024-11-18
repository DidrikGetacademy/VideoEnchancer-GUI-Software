# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['learnreflectai_main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
    (r'C:\Users\didri\Desktop\LearnReflect VideoEnchancer\LearnReflectAI.py', 'LearnReflectAI.py'),
    (r'C:\Users\didri\Desktop\LearnReflect VideoEnchancer\Assets\*', 'Assets'),
    (r'C:\Users\didri\Desktop\LearnReflect VideoEnchancer\AI-onnx\*', 'AI-onnx'),
    (r'C:\Users\didri\Desktop\LearnReflect VideoEnchancer\Validate_key.py', 'Validate_key.py'),
    (r'C:\Users\didri\Desktop\LearnReflect VideoEnchancer\activation_window.py', 'activation_window.py'),
    (r'C:\Users\didri\Desktop\LearnReflect VideoEnchancer\Logger.py', 'Logger.py')
    ], 

     hiddenimports=[
    'importlib_resources.trees', 
    'pkg_resources._vendor.jaraco.functools',
    "_frozen_importlib_external",  # Required for importlib
    "importlib",                   # Optional, included for importlib
    "importlib.abc",               # Optional, for importlib abstraction
    "zipimport",                   # Top-level module related to zip files
    "pwd",                         # For POSIX systems (e.g., Linux/macOS)
    "grp",                         # For POSIX systems (group-related functions)
    "posix",                       # For POSIX systems, part of os module
    "resource",                    # For POSIX systems, related to system resources
    "_scproxy",                    # For urllib on macOS (proxy support)
    "termios",                     # For terminal I/O, especially on UNIX-like systems
    "multiprocessing.BufferTooShort",  # For multiprocessing support
    "multiprocessing.AuthenticationError",  # For authentication-related issues in multiprocessing
    "_posixshmem",                 # For POSIX-based shared memory in multiprocessing
    "_posixsubprocess",            # For subprocess handling on POSIX systems
    "multiprocessing.get_context",  # For getting multiprocessing contexts
    "multiprocessing.TimeoutError",  # For timeout handling in multiprocessing
    "multiprocessing.set_start_method",  # For setting start method in multiprocessing
    "multiprocessing.get_start_method",  # For getting start method in multiprocessing
    "distutils.sysconfig",         # For distutils configuration handling
    "distutils",                   # Distutils runtime modules
    "setuptools._distutils.util",  # Util functions for distutils in setuptools
    "setuptools._distutils.command.build_ext",  # Build extensions with distutils
    "setuptools._distutils.command.build_scripts",  # Build scripts with distutils
    "setuptools._distutils.cygwinccompiler",  # Cygwin compiler for distutils
    "setuptools._distutils.tests",  # Distutils tests in setuptools
    "setuptools._distutils.tests.test_build_ext",  # Test distutils build extensions
    "setuptools._distutils.tests.test_build_scripts",  # Test distutils build scripts
    "setuptools._distutils.tests.test_cygwinccompiler",  # Test Cygwin compiler
    "setuptools._distutils.tests.test_install",  # Test distutils installation
    "setuptools._distutils.tests.test_mingwccompiler",  # Test MinGW compiler
    "setuptools._distutils.tests.test_sysconfig",  # Test sysconfig in distutils
    "setuptools._distutils.tests.test_unixccompiler",  # Test UNIX compiler
    "setuptools._distutils.tests.test_util",  # Test utility functions in distutils
    # Missing modules:
    "cffi._pycparser",  # For cffi support
    "defusedxml",  # For PIL.Image support
    "pickle5",  # For numpy compatibility
    "numpy.eye",  # For numpy support
    "numpy.core.integer",  # For numpy core
    "numpy.core.conjugate",  # For numpy core
    "numpy.core.ufunc",  # For numpy core
    "numpy.core.ones",  # For numpy core
    "numpy.core.hstack",  # For numpy core
    "numpy.core.atleast_1d",  # For numpy core
    "numpy.core.atleast_3d",  # For numpy core
    "numpy.core.vstack",  # For numpy core
    "numpy.core.linspace",  # For numpy core
    "numpy.core.transpose",  # For numpy core
    "numpy.core.result_type",  # For numpy core
    "numpy.core.float_",  # For numpy core
    "numpy.core.number",  # For numpy core
    "numpy.core.max",  # For numpy core
    "numpy.core.bool_",  # For numpy core
    "numpy.core.inf",  # For numpy core
    "numpy.core.array2string",  # For numpy core
    "numpy.core.signbit",  # For numpy core
    "numpy.core.isscalar",  # For numpy core
    "numpy.core.isnat",  # For numpy core
    "numpy.core.ndarray",  # For numpy core
    "numpy.core.array_repr",  # For numpy core
    "numpy.core.arange",  # For numpy core
    "numpy.core.float32",  # For numpy core
    "numpy.core.iinfo",  # For numpy core
    "numpy.core.reciprocal",  # For numpy core
    "numpy.core.sort",  # For numpy core
    "numpy.core.argsort",  # For numpy core
    "numpy.core.sign",  # For numpy core
    "numpy.core.isnan",  # For numpy core
    "numpy.core.count_nonzero",  # For numpy core
    "numpy.core.divide",  # For numpy core
    "numpy.core.swapaxes",  # For numpy core
    "numpy.core.matmul",  # For numpy core
    "numpy.core.object_",  # For numpy core
    "numpy.core.asanyarray",  # For numpy core
    "numpy.core.intp",  # For numpy core
    "numpy.core.atleast_2d",  # For numpy core
    "numpy.core.prod",  # For numpy core
    "numpy.core.amax",  # For numpy core
    "numpy.core.amin",  # For numpy core
    "numpy.core.moveaxis",  # For numpy core
    "numpy.core.geterrobj",  # For numpy core
    "numpy.core.errstate",  # For numpy core
    "numpy.core.finfo",  # For numpy core
    "numpy.core.isfinite",  # For numpy core
    "numpy.core.sum",  # For numpy core
    "numpy.core.sqrt",  # For numpy core
    "numpy.core.multiply",  # For numpy core
    "numpy.core.add",  # For numpy core
    "numpy.core.dot",  # For numpy core
    "numpy.core.Inf",  # For numpy core
    "numpy.core.all",  # For numpy core
    "numpy.core.newaxis",  # For numpy core
    "numpy.core.complexfloating",  # For numpy core
    "numpy.core.inexact",  # For numpy core
    "numpy.core.cdouble",  # For numpy core
    "numpy.core.csingle",  # For numpy core
    "numpy.core.double",  # For numpy core
    "numpy.core.single",  # For numpy core
    "numpy.core.intc",  # For numpy core
    "numpy.core.empty_like",  # For numpy core
    "numpy.core.empty",  # For numpy core
    "numpy.core.zeros",  # For numpy core
    "numpy.core.asarray",  # For numpy core
    "numpy.core.array",  # For numpy core
    "numpy.dtype",  # For numpy core
    "numpy.bool_",  # For numpy core
    "numpy.recarray",  # For numpy core
    "numpy.histogramdd",  # For numpy core
    "numpy.expand_dims",  # For numpy core
    "numpy.iscomplexobj",  # For numpy core
    "numpy.amin",  # For numpy core
    "numpy.amax",  # For numpy core
    "threadpoolctl",  # For numpy optional functionality
    "numpy.lib.imag",  # For numpy lib
    "numpy.lib.real",  # For numpy lib
    "numpy.lib.iscomplexobj",  # For numpy lib
    "numpy.ufunc",  # For numpy
    "psutil",  # For numpy optional functionality
    "win32pdh",  # For Windows support in numpy
    "numpy.isinf",  # For numpy
    "numpy.isnan",  # For numpy
    "numpy.isfinite",  # For numpy
    "numpy.float64",  # For numpy typing
    "numpy.float32",  # For numpy typing
    "numpy.uint64",  # For numpy typing
    "numpy.uint32",  # For numpy typing
    "numpy.uint16",  # For numpy typing
    "numpy.uint8",  # For numpy typing
    "numpy.int64",  # For numpy typing
    "numpy.int32",  # For numpy typing
    "numpy.int16",  # For numpy typing
    "numpy.int8",  # For numpy typing
    "numpy.bytes_",  # For numpy typing
    "numpy.str_",  # For numpy typing
    "numpy.void",  # For numpy typing
    "numpy.object_",  # For numpy typing
    "numpy.datetime64",  # For numpy typing
    "numpy.timedelta64",  # For numpy typing
    "numpy.number",  # For numpy typing
    "numpy.complexfloating",  # For numpy typing
    "numpy.floating",  # For numpy typing
    "numpy.integer",  # For numpy typing
    "numpy.unsignedinteger",  # For numpy typing
    "numpy.generic",  # For numpy typing
    "numpy._typing._ufunc",  # For numpy typing
    "PyObjCTools",  # For darkdetect on macOS
    "Foundation",  # For darkdetect on macOS
    "AppKit",  # For darkdetect on macOS
    "objc",  # For darkdetect on macOS
    "ctypes",  # For darkdetect on macOS
    "scipy",  # For deep integration with numpy
    "scipy.linalg",  # For deep integration with scipy.linalg
],


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
    name='learnreflectai_main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
