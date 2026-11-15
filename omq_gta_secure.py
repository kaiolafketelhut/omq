"""
OMQ GTA SECURE v1.0 - Phase 3
GTA Gameplay + OMQ Secure Core (EAL4+ TOE)
FCS_COP.1, FDP_SDI.2, FIA_UAU.1, FPT_TST.1, FPT_FLS.1
"""
import sys, os
sys.path.insert(0, "omq_secure/src")
from omq_secure_core import selftest, hash_password, verify_password, save_secure, load_secure, derive_key
import json, hashlib, hmac

print("="*50)
print("👑 OMQ GTA SECURE v1.0 - EAL4+ PHASE 3 🔒")
print("="*50)

# FPT_TST.1 - Selbsttest beim Start, sonst STOP
if not selftest():
    print("FPT_TST.1 FEHLER: TOE manipuliert! Spiel startet NICHT.")
    sys.exit(1)

# FIA_UAU.1 - Login
PW_FILE = "omq_secure_pw.json"
if os.path.exists(PW_FILE):
    with open(PW_FILE) as f:
        stored = json.load(f)
    pw = input("Passwort (Secure Login): ")
    if not verify_password(pw, stored):
        print("FIA_UAU.1: Falsches Passwort! Zugang verweigert.")
        sys.exit(1)
    print("Login OK! Willkommen zurück, Milliardär! 👑")
else:
    print("Neuer Spieler! Erstelle Secure Passwort:")
    pw = input("Neues Passwort (min. 8 Zeichen, MERKEN!): ")
    stored = hash_password(pw)
    with open(PW_FILE, "w") as f:
        json.dump(stored, f)
    print("Passwort-Hash gespeichert. NIE im Klartext!")

# FDP_SDI.2 - Savegame laden, nur wenn Signatur OK
data, msg = load_secure(pw)
print(f"[LOAD] {msg}")
if data is None and "Kein Savegame" not in msg and "manipuliert" in msg:
    print("Savegame manipuliert! Starte mit 0$ - Cheater werden bestraft! 😈")
    geld = 0
    punkte = 0
elif data is None:
    geld = 0
    punkte = 0
    print("Neues Secure Savegame gestartet!")
else:
    geld = data.get("geld", 0)
    punkte = data.get("punkte", 0)
    print(f"Savegame geladen: {geld:,} $ | {punkte} Punkte")

print("\nSteuerung:")
print("4 = +26.000.000$ 💰 | 5 = Reset! | 1 = +100 Punkte | 0 = SICHER Speichern + Aussteigen")
print("1.300.000.000$ = MILLIARDÄR! Ziel: 7.569.025.850$ schlagen!")

while True:
    print(f"\n💰 Geld: {geld:,} $ | ⭐ Punkte: {punkte}")
    wahl = input("OMQ SECURE > ").strip()
    if wahl == "4":
        geld += 26000000
        punkte += 10
        print(f"+26.000.000$! Neuer Stand: {geld:,} $")
        if geld >= 1300000000:
            print("🏆 MILLIARDÄR! 1.300.000.000$+ erreicht!")
    elif wahl == "1":
        punkte += 100
        print(f"+100 Punkte! Total: {punkte}")
    elif wahl == "5":
        print("Reset! Geld wird auf 0 gesetzt, aber SECURE gespeichert...")
        geld = 0
        punkte = 0
    elif wahl == "0":
        # FDP_SDI.2 - Sicher speichern mit Signatur
        print(save_secure({"geld": geld, "punkte": punkte, "spiel": "OMQ GTA SECURE"}, pw))
        print(f"Game Over! Du hast {geld:,} $ SECURE gesichert! 🔒")
        print("Niemand kann das fälschen - HMAC-SHA256 schützt dich!")
        break
    else:
        print("Ungültig! Nur 4, 1, 5, 0 - FPT_FLS.1: Sicherer Zustand bleibt!")
