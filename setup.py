from cx_Freeze import setup, Executable

setup(
    name="DhanuCalculator",
    version="1.0",
    description="DhanuFirstCal",
    executables=[Executable("Calci_UI.py", base="Win32GUI")]
)

