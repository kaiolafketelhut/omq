# ADV_FSP.4 - Funktionale Spezifikation
# OMQ Secure Core v1.0 - EAL4+

## TSF Interfaces

### 1. derive_key(password, salt)
- Zweck: FCS_CKM.1 - Key aus Passwort ableiten
- Input: password (string), salt (16 Bytes)
- Output: 32-Byte Key
- Mechanismus: PBKDF2-HMAC-SHA256, 200.000 Iterationen
- Fehler: Kein Fehler, immer deterministisch

### 2. hash_password(password) / verify_password(password, stored)
- Zweck: FIA_UAU.1 - Authentifizierung
- Input: Passwort, gespeicherter Salt+Hash
- Output: True/False
- Mechanismus: hmac.compare_digest - zeitkonstant, kein Timing-Leak
- Fehler: False bei falschem Passwort, keine Info ob User oder Passwort falsch

### 3. save_secure(data, password)
- Zweck: FDP_SDI.2 + Anti-Replay
- Input: dict data, password
- Output: Bestätigungs-String mit Counter + Signatur-Präfix
- Mechanismus: Counter+1, JSON sort_keys, HMAC-SHA256 signieren, Datei omq_save_secure.json
- Fehler: Schreibt nichts bei Exception

### 4. load_secure(password)
- Zweck: FDP_SDI.2 + FPT_FLS.1
- Input: password
- Output: (data, msg) oder (None, Fehler)
- Mechanismus: Signatur prüfen, bei Fehler -> (None, verweigert), KEIN Laden
- Fehlerfälle: Datei fehlt, JSON kaputt, Signatur falsch, Key falsch -> alle verweigert

### 5. selftest()
- Zweck: FPT_TST.1 - Selbsttest
- Input: Keiner
- Output: True/False
- Mechanismus: SHA256 über eigene Datei, Ausgabe Core-Hash Präfix
- Fehler: False, TOE darf dann nicht weiterlaufen
