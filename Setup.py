# Copyright (c) BoosterTool
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.

import subprocess
import sys
import time
import os

def cinematic(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    cinematic("Installing requests...")
    time.sleep(0.5)
    cinematic("Loading menu and files...")
    time.sleep(0.5)

    subprocess.run(
        f'"{sys.executable}" pip install requests',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

if __name__ == "__main__":
    main()
