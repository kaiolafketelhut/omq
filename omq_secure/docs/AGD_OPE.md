# AGD_OPE.1 - Operational User Guidance
# OMQ Secure Core v1.0

## Für Spieler / User
1. Starte: python3 omq_secure/src/omq_secure_core.py
2. Wähle ein STARKES Passwort (min. 12 Zeichen, nie wiederverwenden!)
3. Merke dir das Passwort! Es gibt KEIN Zurücksetzen - ohne Passwort ist Savegame verloren. Das ist so gewollt (EAL4+).
4. Wenn du siehst: "Signatur ungültig! Laden verweigert." -> Savegame wurde manipuliert. NICHT weiter spielen, Datei sichern, Admin kontaktieren.
5. Teile NIE dein Passwort, auch nicht per Screenshot!

## Für Admin / Entwickler
- Niemals Secret Keys in Git committen
- Releases immer signiert taggen: git tag -s
- Bei Bug: Siehe ALC_FLR.1 - Bug in GitHub Issue, Fix, Test, Release
- Counter-Datei nie manuell zurücksetzen - sonst Replay möglich
