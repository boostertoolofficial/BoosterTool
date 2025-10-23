import os
import sys
import time
import shutil
import requests
import random
import webbrowser
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def center(text):
    width = shutil.get_terminal_size().columns
    return text.center(width)

def header():
    clear()
    print("\033[91m")
    print(center("██████╗  ██████╗  ██████╗ ███████╗████████╗███████╗██████╗"))
    print(center("██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗"))
    print(center("██████╔╝██║   ██║██║   ██║███████╗   ██║   █████╗  ██████╔╝"))
    print(center("██╔══██╗██║   ██║██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗"))
    print(center("██████╔╝╚██████╔╝╚██████╔╝███████║   ██║   ███████╗██║  ██║"))
    print(center("╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝"))
    print(center("owner: lorepro44 xerpp_"))
    print("\033[0m\n")

def menu():
    print("╔════════════════════════════════════════════════════════╗")
    print("║                    BOOSTER TOOL MENU                   ║")
    print("╠════════════════════════════════════════════════════════╣")
    print("║ [1] Discord Invite Booster                            ║")
    print("║ [2] Discord Nitro Generator                           ║")
    print("║ [3] IP Lookup                                         ║")
    print("║ [4] AutoDox                                           ║")
    print("║ [5] Dox                                               ║")
    print("║ [6] Exit                                              ║")
    print("╚════════════════════════════════════════════════════════╝")

def discord_invite_booster():
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
    usernames = []
    for _ in range(1000):
        name = random.choice(base_names) + random.choice(base_names)
        tag = str(random.randint(1000, 9999))
        usernames.append(f"{name}#{tag}")

    for i in range(5):
        user = random.choice(usernames)
        print(f"Boosting server... User: {user}")
        time.sleep(0.6)

    print("\n✅ Inviti simulati completati.")
    input("\nPremi Invio per tornare al menu...")

def nitro_generator():
    print("\n🎁 Generatore di codici Discord Nitro")
    try:
        count = int(input("🔢 Quanti codici vuoi generare? > "))
        print("\n🎉 Codici generati:")
        codes = []
        for _ in range(count):
            code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=16))
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
    print("\n🔍 IP Lookup OSINT Mode")
    ip = input("🔢 Inserisci l'indirizzo IP da analizzare: ").strip()

    try:
        headers = {"User-Agent": "BoosterTool/1.0"}
        response = requests.get(f"https://ipinfo.io/{ip}/json", headers=headers, timeout=5)
        if response.status_code != 200:
            raise ValueError("IP non valido o non trovato.")

        data = response.json()
        ip = data.get("ip", ip)
        country_code = data.get("country", "Unknown")
        region = data.get("region", "Unknown")
        city = data.get("city", "Unknown")
        org = data.get("org", "").lower()
        loc = data.get("loc", "")

        countries = {
            "IT": "Italy", "RU": "Russia", "US": "United States", "FR": "France",
            "DE": "Germany", "BR": "Brazil", "IN": "India", "CN": "China",
            "JP": "Japan", "GB": "United Kingdom", "ES": "Spain", "CA": "Canada",
            "TR": "Turkey", "MX": "Mexico", "AR": "Argentina", "EG": "Egypt",
            "KR": "South Korea", "SA": "Saudi Arabia", "AU": "Australia"
        }
        full_country = countries.get(country_code, "Unknown Country")
        maps_link = f"https://www.google.com/maps/place/{loc}" if loc else "N/A"

        print("\n════════════════════════════════════════════════════════════")
        print(f"IP: {ip}")
        print(f"Location: {city}, {region}, {country_code}")
        print(f"Country: {full_country}")
        print(f"ISP/Org: {org}")
        print(f"Coordinates: {loc}")
        print(f"🌍 Google Maps: {maps_link}")

        suspicious_keywords = ["vpn", "proxy", "hosting", "cloud", "digitalocean", "ovh", "amazon", "azure", "google"]
        if any(keyword in org for keyword in suspicious_keywords):
            print("⚠️ IP sospetto: potrebbe essere una VPN, proxy o datacenter.")
        else:
            print("✅ IP sembra residenziale o non mascherato.")
        print("════════════════════════════════════════════════════════════")
    except Exception as e:
        print("❌ Errore durante il recupero dell'IP.")
        print(f"Dettagli: {e}")
    input("\nPremi Invio per tornare al menu...")

def autodox():
    print("\n🧠 AutoDox in corso...")
    time.sleep(1)

    folder = "files"
    os.makedirs(folder, exist_ok=True)

    filename = os.path.join(folder, "AutoDox.bat")
    bat_script = """@echo off

REM privacy_audit.bat - per uso personale
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

    print("✅ AutoDox salvato nella cartella 'files' come 'AutoDox (Run Me!).bat'")
    input("\nPremi Invio per tornare al menu...")

def dox():
    print("\n📁 Dox in sviluppo...")
    input("Premi Invio per tornare al menu...")

def handle_choice(choice):
    if choice == "1":
        discord_invite_booster()
    elif choice == "2":
        nitro_generator()
    elif choice == "3":
        ip_lookup()
    elif choice == "4":
        autodox()
    elif choice == "5":
        dox()
    elif choice == "6":
        print("\n👋 Uscita...")
        time.sleep(1)
        sys.exit()
    else:
        print("\n❌ Opzione non valida.")
        time.sleep(1)

def main():
    while True:
        header()
        menu()
        try:
            choice = input("\ntool@booster > ").strip()
            handle_choice(choice)
        except KeyboardInterrupt:
            print("\n⛔ Interruzione manuale. Uscita...")
            sys.exit()

if __name__ == "__main__":
    main()
