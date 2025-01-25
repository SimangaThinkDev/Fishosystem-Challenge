import platform
import os

def clear():
    if "windows" in platform.system().lower():
        os.system("cls")
    else:
        os.system("clear")