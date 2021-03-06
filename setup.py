import sys
from setuptools import setup
from io import open

from cx_Freeze import setup, Executable

from pre_build import build_qt

# Build qt related resources
build_qt()

# Setup cx_freeze packaging
base = None
includefiles = None
if sys.platform == "win32":
    includefiles = [
            ("C:\Python33\Lib\site-packages\PyQt5\plugins\platforms\qwindows.dll", "platforms\qwindows.dll"),
            ("pomito\\plugins\\ui\\wintaskbar.tlb", "wintaskbar.tlb"),
        ]

includefiles += [
    ("docs\\sample_config.ini", "docs\\sample_config.ini"),
    ("docs\\sample_todo.txt", "docs\\sample_todo.txt"),
]

buildOptions = dict(packages = [],
        excludes = [],
        includes = [
            "atexit",
            "sip",
        ],
        include_files = includefiles,
        )

executables = [Executable('pomito.py', base = base)]

setup(
    name='Pomito',
    version='0.1.0',
    author='Arun Mahapatra',
    packages=['pomito'],
    scripts=['pomito.py'],
    url='https://www.github.com/codito/pomito',
    license='LICENSE',
    description='Simple pomodoro timer with support for tasks and hooks',
    long_description=open('README.md').read(),
    install_requires=[
        "pywin32==218",
        "peewee==2.1.4",
        "pyrtm==0.4.1",
        "blinker==1.3",
        "comtypes==0.6.2",
        "cx-freeze==4.3.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Utilities",
    ],
    test_suite='py.test',
    tests_require=[
        "pyfakefs==2.2",
        "pytest==2.3.5",
        "pytest-cov==1.6",
        "sure==1.2.2",
    ],
    options = dict(build_exe = buildOptions),
    executables = executables
)
