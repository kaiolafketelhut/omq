# ADV_TDS.3 - Design Dokument
# OMQ Secure Core v1.0 - EAL4+

## Architektur - 3 Schichten

### Schicht 1: Krypto-Schicht (FCS)
- derive_key() - PBKDF2
- HMAC-SHA256 für Signatur
- os.urandom(16) für Salt - CSPRNG des OS
- Kein Key im Klartext im Code! Key lebt nur im RAM, nur abgeleitet aus Passwort.

### Schicht 2: Zugriffs-Schicht (FDP / FIA)
- hash_password / verify_password - Auth
- save_secure / load_secure - Zugriff nur nach Verifizierung
- Counter-Datei - Anti-Replay, monoton steigend
- FPT_FLS.1: Bei jedem Fehler -> sicherer Zustand = NICHT laden

### Schicht 3: Selbsttest-Schicht (FPT)
- selftest() - Hash über eigene Datei
- Wird bei jedem Start aufgerufen
- Bei Fehler: TOE stoppt

## Datenfluss
Passwort -> PBKDF2 -> Key (RAM) -> HMAC über Payload -> Savegame-Datei
Laden: Datei -> HMAC prüfen mit Key -> nur bei OK -> Daten zurück

## Abhängigkeiten
- Python 3.9+ hashlib, hmac, json, os, time - nur Standard-Library, keine externen Pakete
- OS CSPRNG für Salt
- Dateisystem für Savegame + Counter
