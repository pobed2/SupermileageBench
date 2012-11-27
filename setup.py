import cx_Freeze
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

buildOptions = dict(
    excludes=["Tkinter"])

executables = [
    cx_Freeze.Executable("main_class.py", base=base)
]

cx_Freeze.setup(
    name="test_bench",
    version="0.0.0",
    description="CxFreeze Test",
    executables=executables,
    options=dict(build_exe=buildOptions))

