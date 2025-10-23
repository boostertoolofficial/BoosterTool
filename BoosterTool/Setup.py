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
