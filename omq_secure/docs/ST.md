# Security Target - OMQ Secure Core v1.0
# EAL4 + ALC_FLR.1 + AVA_VAN.4
# Common Criteria ISO/IEC 15408

## 1. ST Introduction
- ST Reference: OMQ-ST-1.0
- TOE Reference: OMQ Secure Core v1.0
- TOE Type: Software - Game Security Core
- CC Version: 3.1 Rev 5
- Assurance: EAL4 augmented with ALC_FLR.1, AVA_VAN.4
- Developer: Kai Olaf Ketelhut / OMQ GOLD

## 2. TOE Description
OMQ Secure Core schützt OMQ Spielstände vor Manipulation.

TOE Bestandteile:
- omq_secure_core.py - Kern: Signatur, Verschlüsselung, Integritäts-Check
- Savegame-Manager: Speichern / Laden nur mit gültiger Signatur
- Auth-Modul: Spieler-Login mit Passwort-Hash (Argon2 / PBKDF2)
- Anti-Tamper: Selbsttest beim Start, erkennt geänderten Code

NICHT im TOE: Grafik, GTA-Spiellogik, Webseite, GitHub Releases.

## 3. Threats - Angreifer: Spieler mit Root-Zugriff
- T.FAKE_SAVE: Angreifer fälscht Geldstand in Savegame, z.B. 999.999.999$ eintragen
- T.TAMPER_CODE: Angreifer ändert Code, um Sicherheits-Checks zu umgehen
- T.REPLAY: Angreifer spielt altes Savegame wieder ein, um Geld zu duplizieren
- T.BRUTEFORCE: Angreifer rät Passwort durch viele Versuche
- T.REVERSE: Angreifer liest Secret Key aus Code aus

## 4. Security Objectives
- O.INTEGRITY: Savegames müssen manipulationssicher sein
- O.AUTH: Nur authentifizierter Spieler darf laden / speichern
- O.ANTI_REPLAY: Altes Savegame darf nicht wieder eingespielt werden
- O.SELFTEST: TOE erkennt Manipulation an sich selbst beim Start
- O.SECRETS: Keys dürfen nicht im Klartext im Code stehen

## 5. Security Functional Requirements (SFRs)
- FCS_COP.1 - Kryptographische Operationen: HMAC-SHA256, AES-256-GCM
- FCS_CKM.1 / FCS_CKM.4 - Key Generation / Key Destruction
- FIA_UAU.1 / FIA_UAU.5 - Authentifizierung, Passwort + Rate-Limit
- FIA_AFL.1 - Nach 5 Fehlversuchen 60s Sperre
- FDP_ACC.1 / FDP_ACF.1 - Zugriffskontrolle auf Savegames
- FDP_SDI.2 - Integrität überwachter Daten
- FPT_TST.1 - Selbsttests beim Start
- FPT_FLS.1 - Sicherer Zustand bei Fehler: Kein Laden bei ungültiger Signatur
- FTA_SSL.3 - Session-Timeout nach 15 Min Inaktivität

## 6. Security Assurance Requirements (SARs)
EAL4 + Augmentierung:
- ADV_ARC.1, ADV_FSP.4, ADV_IMP.1, ADV_TDS.3
- AGD_OPE.1, AGD_PRE.1
- ALC_CMC.4, ALC_CMS.4, ALC_DEL.1, ALC_DVS.1, ALC_FLR.1, ALC_LCD.1, ALC_TAT.1
- ASE_CCL.1, ASE_ECD.1, ASE_INT.1, ASE_OBJ.2, ASE_REQ.2, ASE_SPD.1, ASE_TSS.1
- ATE_COV.2, ATE_DPT.1, ATE_FUN.1, ATE_IND.2
- AVA_VAN.4 - Systematische Schwachstellen-Analyse, hoher Angriffswiderstand
- ALC_FLR.1 - Flaw Remediation: Bugfix-Prozess dokumentiert

## 7. TOE Summary Specification
- Savegame wird mit HMAC-SHA256 signiert (Key aus Passwort abgeleitet via PBKDF2)
- Nonce + Counter gegen Replay
- Beim Laden: Signatur prüfen, bei Fehler -> Abbruch, kein Laden
- Beim Start: Hash über eigene Dateien prüfen
- Passwort wird nie im Klartext gespeichert, nur Salt+Hash
