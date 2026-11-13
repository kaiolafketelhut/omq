import os
w = os.environ.get("INPUT_WAHL", "5")
spiele = {"1":"EAL310 Klassik","2":"EAL311 Du rätst","3":"EAL312 Schwierigkeit","4":"EAL313 Duell","5":"EAL314 Turnier"}
print(f"=== EAL315 OMQ MENÜ ===")
print(f"Gewählt: {spiele.get(w,'Turnier')}")
print("🏆 Alle 5 Spiele in einem! OMQ!")
