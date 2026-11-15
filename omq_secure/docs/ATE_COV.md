# ATE_COV.2 + ATE_DPT.1 - Test Coverage
# OMQ Secure Core v1.0

## Coverage-Tabelle
| SFR | Funktion | Test | Ergebnis |
| FCS_COP.1 | derive_key + HMAC | test 3/5 Save/Load | PASS |
| FIA_UAU.1 | verify_password | test 2/5 Login | PASS |
| FDP_SDI.2 | save/load Signatur | test 3/5 + 4/5 Tamper | PASS |
| FPT_TST.1 | selftest | test 1/5 | PASS |
| FPT_FLS.1 | Laden verweigern bei Fehler | test 4/5 + 5/5 | PASS |
| FDP_ACC.1 | Nur mit Passwort laden | test 5/5 | PASS |

## Coverage: 6/6 SFRs getestet = 100% Funktions-Coverage
## Tiefe: ATE_DPT.1 - Tests greifen auf Modul-Ebene (nicht nur UI)
