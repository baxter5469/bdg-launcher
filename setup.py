import sys
import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\local_to_python\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\local_to_python\\Python35-32\\tcl\\tk8.6"

base = 'Win32GUI'

executables = [cx_Freeze.Executable("main.py", base= "Win32GUI")]

cx_Freeze.setup(
    name = "BDG Launcher",
    version = "1.0",
    options = {"launcher.exe":{"packages":["numpy"]}},
    executables = executables
)
