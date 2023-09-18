import keyboard
import os
import time

from colorama import just_fix_windows_console
from termcolor import cprint


def cls():
    os.system("cls" if os.name == "nt" else "clear")

def PrintStart():
    cls()

    cprint("[!] Press [S] To Start", "blue")
    print()
    cprint("[!] Hold [Esc] To Stop", "blue")

if os.name == "nt":
    os.system("title Anti Afk")

just_fix_windows_console()

PrintStart()

while True:
    if keyboard.is_pressed("s"):
        while True:
            time.sleep(0.5)
            for _ in range(5):
                time.sleep(0.1)
                keyboard.press("w")
            time.sleep(0.2)
            for _ in range(5):
                time.sleep(0.1)
                keyboard.press("a")
            time.sleep(0.2)
            for _ in range(5):
                time.sleep(0.1)
                keyboard.press("s")
            time.sleep(0.2)
            for _ in range(5):
                time.sleep(0.1)
                keyboard.press("d")

            if keyboard.is_pressed("esc"):
                break