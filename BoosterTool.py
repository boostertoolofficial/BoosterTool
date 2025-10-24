# Copyright (c) BoosterTool
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.

import os
import sys
import time
import shutil
import requests
import random
import webbrowser
import string
import threading

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def center(text):
    width = shutil.get_terminal_size().columns
    return text.center(width)

def loading_bar():
    clear()
    print("\n🔧 Avvio BoosterTool in corso...\n")
    bar_length = 30
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = "[" + "#" * i + "-" * (bar_length - i) + f"] {percent}%"
        print(center(bar), end="\r", flush=True)
        time.sleep(0.07)
    print(center("[##############################] 100%"))
    print(center("✅ Caricamento completato.\n"))
    time.sleep(1)

def header():
    clear()
    print("\033[91m")
    print(center("██████╗  ██████╗  ██████╗ ███████╗████████╗███████╗██████╗"))
    print(center("██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗"))
    print(center("██████╔╝██║   ██║██║   ██║███████╗   ██║   █████╗  ██████╔╝"))
    print(center("██╔══██╗██║   ██║██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗"))
    print(center("██████╔╝╚██████╔╝╚██████╔╝███████║   ██║   ███████╗██║  ██║"))
    print(center("╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝"))
    print("\033[0m\n")

def menu():
    print("\033[0m\n")
    print("╔════════════════════════════════════════════════════════╗")
    print("║                    BOOSTER TOOL MENU                   ║")
    print("╠════════════════════════════════════════════════════════╣")
    print("║ [01] Discord Invite Booster                            ║")
    print("║ [02] Discord Nitro Generator                           ║")
    print("║ [03] IP Lookup                                         ║")
    print("║ [04] Autod0x                                           ║")
    print("║ [05] d0x                                               ║")
    print("║ [06] Discord Token Generator                           ║")
    print("║ [07] Exit                                              ║")
    print("╚════════════════════════════════════════════════════════╝")
    print("\033[0m\n")

def discord_invite_booster():
    clear()
    header()
    print("\n🚀 Discord Invite Booster")
    invite = input("🔗 Invite: ").strip()
    print(f"\n🔗 Collegamento ricevuto: {invite}")
    time.sleep(0.5)

    print("\n👥 Joining users...")
    time.sleep(1)

    base_names = [
        "Shadow", "Pixel", "Nova", "Luna", "Ghost", "Neo", "Crimson", "Echo",
        "Sky", "Dark", "Frost", "Cyber", "Venom", "Star", "Iron", "Void",
        "Flare", "Claw", "Byte", "Blade", "Spark", "Knight", "Pulse", "Wolf"
    ]
    for i in range(5):
        name = random.choice(base_names) + random.choice(base_names)
        tag = str(random.randint(1000, 9999))
        print(f"🚀 Boosting server... User: {name}#{tag}")
        time.sleep(0.6)

    print("\n✅ Inviti simulati completati.")
    input("\nPremi Invio per tornare al menu...")

def nitro_generator():
    clear()
    header()
    print("\n🎁 Generatore di codici Discord Nitro")
    try:
        count = int(input("🔢 Quanti codici vuoi generare? > "))
        print("\n🎉 Codici generati:")
        codes = []
        for _ in range(count):
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            url = f"https://discord.gift/{code}"
            codes.append(url)
            print(url)

        open_all = input("\n🌐 Vuoi aprire tutte le schede nel browser? (s/n) > ").strip().lower()
        if open_all == "s":
            print("\n🚀 Apertura schede in corso...")
            for url in codes:
                webbrowser.open_new_tab(url)
                time.sleep(0.3)

        print("\n✅ Generazione completata.")
    except ValueError:
        print("❌ Inserisci un numero valido.")
    input("\nPremi Invio per tornare al menu...")

def ip_lookup():
    clear()
    header()
    print("\n🔍 IP Lookup OSINT Mode")
    ip = input("🔢 Inserisci l'indirizzo IP da analizzare: ").strip()

    try:
        headers = {"User-Agent": "BoosterTool/1.0"}
        response = requests.get(f"https://ipinfo.io/{ip}/json", headers=headers, timeout=5)
        data = response.json()

        loc = data.get("loc", "N/A")
        maps_link = f"https://www.google.com/maps/place/{loc}" if loc != "N/A" else "N/A"

        print("\n════════════════════════════════════════════════════════════")
        print(f"IP: {data.get('ip', ip)}")
        print(f"Location: {data.get('city', 'Unknown')}, {data.get('region', 'Unknown')}, {data.get('country', 'Unknown')}")
        print(f"ISP/Org: {data.get('org', 'Unknown')}")
        print(f"Coordinates: {loc}")
        print(f"🌍 Google Maps: {maps_link}")
        print("════════════════════════════════════════════════════════════")
    except Exception as e:
        print("❌ Errore durante il recupero dell'IP.")
        print(f"Dettagli: {e}")
    input("\nPremi Invio per tornare al menu...")

def autod0x():
    clear()
    header()
    print("\n🧠 Autod0x in corso...")
    time.sleep(1)

    folder = "files"
    os.makedirs(folder, exist_ok=True)

    filename = os.path.join(folder, "AutoDox (Run Me!).bat")
    bat_script = """@echo off
setlocal
set LOGFILE=%~dp0privacy_audit_%COMPUTERNAME%_%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%.txt
echo ===== Privacy audit - %DATE% %TIME% ===== > "%LOGFILE%"
echo Hostname: %COMPUTERNAME% >> "%LOGFILE%"
echo User: %USERNAME% >> "%LOGFILE%"
echo. >> "%LOGFILE%"
echo --- IP configuration --- >> "%LOGFILE%"
ipconfig /all >> "%LOGFILE%" 2>&1
echo. >> "%LOGFILE%"
echo --- Network connections (listening) --- >> "%LOGFILE%"
netstat -an | find "LISTEN" >> "%LOGFILE%" 2>&1
echo. >> "%LOGFILE%"
echo --- Account info --- >> "%LOGFILE%"
whoami /all >> "%LOGFILE%" 2>&1
echo. >> "%LOGFILE%"
echo --- System info --- >> "%LOGFILE%"
systeminfo >> "%LOGFILE%" 2>&1
echo. >> "%LOGFILE%"
echo Audit completato. Log salvato in: %LOGFILE%
pause
endlocal
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bat_script)

    print("✅ Autod0x salvato nella cartella 'files' come 'AutoDox (Run Me!).bat'")
    input("\nPremi Invio per tornare al menu...")

def d0x():
    clear()
    header()
    print("\n📁 d0x manuale in sviluppo...")
    input("\nPremi Invio per tornare al menu...")

def discord_token_generator():
    clear()
    header()
    print("\n🔐 Discord Token Generator")
    try:
        threads_number = int(input("🔢 Quanti thread vuoi avviare? > "))
    except:
        print("❌ Inserisci un numero valido.")
        input("\nPremi Invio per tornare al menu...")
        return

    def token_check():
        first = ''.join(random.choices(string.ascii_letters + string.digits + '-' + '_', k=random.choice([24, 26])))
        second = ''.join(random.choices(string.ascii_letters + string.digits + '-' + '_', k=6))
        third = ''.join(random.choices(string.ascii_letters + string.digits + '-' + '_', k=38))
        token = f"{first}.{second}.{third}"

        try:
            response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token})
            if response.status_code == 200 and "username" in response.text:
                print(f"✅ Valid Token: {token}")
            else:
                print(f"❌ Invalid Token: {token}")
        except:
            print(f"⚠️ Errore durante il check: {token}")

    def request():
        threads = []
        for _ in range(threads_number):
            t = threading.Thread(target=token_check)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()

    request()
    input("\nPremi Invio per tornare al menu...")

def handle_choice(choice):
    if choice == "1":
        discord_invite_booster()
    elif choice == "2":
        nitro_generator()
    elif choice == "3":
        ip_lookup()
    elif choice == "4":
        autod0x()
    elif choice == "5":
        d0x()
    elif choice == "6":
        discord_token_generator()
    elif choice == "7":
        discord_invite_booster()
    elif choice == "02":
        nitro_generator()
    elif choice == "03":
        ip_lookup()
    elif choice == "04":
        autod0x()
    elif choice == "05":
        d0x()
    elif choice == "06":
        discord_token_generator()
    elif choice == "07":
        print("\n👋 Uscita...")
        time.sleep(1)
        sys.exit()
    else:
        print("\n❌ Opzione non valida.")
        time.sleep(1)

def main():
    loading_bar()
    while True:
        header()
        menu()
        try:
            choice = input("\nTool@booster > ").strip()
            handle_choice(choice)
        except KeyboardInterrupt:
            print("\n⛔ Interruzione manuale. Uscita...")
            sys.exit()

if __name__ == "__main__":
    main()
