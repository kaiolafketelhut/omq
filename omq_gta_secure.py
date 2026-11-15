"""
OMQ GTA SECURE v1.1 - Phase 5
GTA + Secure Core + FIA_AFL.1 Rate-Limit + Externe Signatur
"""
import sys, os
sys.path.insert(0, "omq_secure/src")
from omq_secure_core import selftest, hash_password, verify_password, save_secure, load_secure
from rate_limit import check_lock, record_fail, reset_lock
import json

print("="*50)
print("OMQ GTA SECURE v1.1 - EAL4+ PHASE 5 - FIA_AFL.1")
print("="*50)

if not selftest():
    print("FPT_TST.1 FEHLER: TOE manipuliert! Spiel startet NICHT.")
    sys.exit(1)

# FIA_AFL.1 - Sperre prüfen VOR Login
if check_lock():
    sys.exit(1)

PW_FILE = "omq_secure_pw.json"
if os.path.exists(PW_FILE):
    with open(PW_FILE) as f:
        stored = json.load(f)
    pw = input("Passwort (Secure Login): ")
    if not verify_password(pw, stored):
        record_fail()
        print("FIA_UAU.1: Falsches Passwort! Zugang verweigert.")
        sys.exit(1)
    reset_lock()
    print("Login OK! Willkommen zurück, Milliardär!")
else:
    print("Neuer Spieler! Erstelle Secure Passwort:")
    pw = input("Neues Passwort (min. 8 Zeichen, MERKEN!): ")
    stored = hash_password(pw)
    with open(PW_FILE, "w") as f:
        json.dump(stored, f)
    print("Passwort-Hash gespeichert. NIE im Klartext!")

data, msg = load_secure(pw)
print(f"[LOAD] {msg}")
if data is None and "manipuliert" in msg:
    print("Savegame manipuliert! Starte mit 0$ - Cheater werden bestraft!")
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

print("\nSteuerung: 4 = +26.000.000$ | 1 = +100 Punkte | 5 = Reset | 0 = SICHER Speichern + Aussteigen")
print("Ziel: 1.300.000.000$ = MILLIARDÄR!")

while True:
    print(f"\nGeld: {geld:,} $ | Punkte: {punkte}")
    wahl = input("OMQ SECURE > ").strip()
    if wahl == "4":
        geld += 26000000
        punkte += 10
        print(f"+26.000.000$! Neuer Stand: {geld:,} $")
        if geld >= 1300000000:
            print("MILLIARDÄR! 1.300.000.000$+ erreicht!")
    elif wahl == "1":
        punkte += 100
        print(f"+100 Punkte! Total: {punkte}")
    elif wahl == "5":
        print("Reset! Geld auf 0, aber SECURE gespeichert...")
        geld = 0
        punkte = 0
    elif wahl == "0":
        print(save_secure({"geld": geld, "punkte": punkte, "spiel": "OMQ GTA SECURE v1.1"}, pw))
        print(f"Game Over! Du hast {geld:,} $ SECURE gesichert!")
        break
    else:
        print("Ungültig! Nur 4, 1, 5, 0")
