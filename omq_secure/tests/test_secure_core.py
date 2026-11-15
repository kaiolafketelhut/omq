"""
ATE_FUN.1 - Funktionale Tests für OMQ Secure Core v1.0
"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from omq_secure_core import hash_password, verify_password, save_secure, load_secure, selftest

print("ATE_FUN.1 - OMQ Secure Core Tests")
assert selftest() == True
print("PASS 1/5 - FPT_TST.1 Selbsttest")

stored = hash_password("TestPass123!")
assert verify_password("TestPass123!", stored) == True
assert verify_password("Falsch123!", stored) == False
print("PASS 2/5 - FIA_UAU.1 Login richtig/falsch")

print(save_secure({"geld": 5000}, "TestPass123!"))
data, msg = load_secure("TestPass123!")
assert data["geld"] == 5000
print("PASS 3/5 - FDP_SDI.2 Save/Load OK:", msg)

# TAMPER TEST - Angreifer ändert Geldstand!
with open("omq_save_secure.json") as f:
    tampered = json.load(f)
tampered["payload"]["data"]["geld"] = 999999999
with open("omq_save_secure.json", "w") as f:
    json.dump(tampered, f)
data2, msg2 = load_secure("TestPass123!")
assert data2 is None, "TAMPER MUSS ABGELEHNT WERDEN!"
print("PASS 4/5 - FDP_SDI.2 Tamper erkannt:", msg2)

# FALSCHES PASSWORT TEST
print(save_secure({"geld": 100}, "TestPass123!"))
data3, msg3 = load_secure("AnderesPass!")
assert data3 is None
print("PASS 5/5 - Falsches Passwort abgelehnt:", msg3)
print("\nALLE 5 TESTS BESTANDEN! ATE_FUN.1 OK!")
