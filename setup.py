import sys
from cx_Freeze import setup, Executable
import tkinter

base = None
icon = "Logo.ico"

if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("Sorte.py", base=base, icon=icon)]

buildOptions = dict (
    packages = [],
    includes = ["tkinter"],
    include_files = [],
    excludes = []
)

setup(name ="JOGOS LOTERIA",
      version = "1.0",
      description = "My GUI Application!",
      options = dict(build_exe = buildOptions),
      executables = executables
      )
