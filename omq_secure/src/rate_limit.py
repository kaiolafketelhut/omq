"""
FIA_AFL.1 - Rate Limit: Nach 5 Fehlversuchen 60s Sperre
Fix für AVA_VAN-02
"""
import time, json, os
FILE = "omq_secure_lock.json"
def check_lock() -> bool:
    # True = gesperrt, False = darf versuchen
    try:
        with open(FILE) as f:
            d = json.load(f)
        if d["fails"] >= 5 and time.time() - d["last"] < 60:
            print(f"FIA_AFL.1: GESPERRT! Noch {int(60-(time.time()-d['last']))}s warten! 5 Fehlversuche!")
            return True
        if time.time() - d["last"] >= 60:
            reset_lock()
        return False
    except:
        return False
def record_fail():
    try:
        with open(FILE) as f:
            d = json.load(f)
    except:
        d = {"fails": 0, "last": 0}
    d["fails"] += 1
    d["last"] = time.time()
    with open(FILE, "w") as f:
        json.dump(d, f)
    print(f"FIA_AFL.1: Fehlversuch {d['fails']}/5")
def reset_lock():
    if os.path.exists(FILE):
        os.remove(FILE)
