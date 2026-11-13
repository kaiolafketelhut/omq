import random, json, os

DATEI = "omq_statistik.json"

def laden():
    if os.path.exists(DATEI):
        return json.load(open(DATEI))
    return {"spiele":0, "siege_du":0, "siege_pc":0, "bester_versuch":999, "total_versuche":0}

def speichern(s):
    json.dump(s, open(DATEI,"w"), indent=2)

s = laden()
print("=== OMQ EAL316 - STATISTIK ===")
print("Kai Olaf Ketelhut - Berlin")
print(f"Bis jetzt: {s['spiele']} Spiele | Siege DU: {s['siege_du']} | Siege PC: {s['siege_pc']} | Bester Versuch: {s['bester_versuch'] if s['bester_versuch']!=999 else '-'}")
print("")

def pc_versuche(zahl):
    low, high, n = 1, 100, 0
    while low <= high:
        tipp=(low+high)//2; n+=1
        if tipp < zahl: low=tipp+1
        elif tipp > zahl: high=tipp-1
        else: return n

# 1 Duell spielen
zahl = random.randint(1,100); n=0
print("DUELL! Rate 1-100")
while True:
    tipp=int(input("Dein Tipp: ")); n+=1
    if tipp < zahl: print("⬆️ ZU KLEIN!")
    elif tipp > zahl: print("⬇️ ZU GROSS!")
    else: break
p = pc_versuche(zahl)
print(f"DU: {n} - PC: {p} - Zahl: {zahl}")

s["spiele"] += 1
s["total_versuche"] += n
if n < s["bester_versuch"]: 
    s["bester_versuch"]=n
    print(f"🎉 NEUER REKORD! Bester Versuch: {n}!")
if n < p: s["siege_du"]+=1; print("🏆 DU GEWINNST!")
elif n > p: s["siege_pc"]+=1; print("🤖 PC GEWINNT!")
else: print("🤝 UNENTSCHIEDEN!")
speichern(s)
print(f"\n=== DEINE KARRIERE ===")
print(f"Spiele: {s['spiele']} | DU: {s['siege_du']} | PC: {s['siege_pc']} | Best: {s['bester_versuch']} | Schnitt: {s['total_versuche']/s['spiele']:.1f}")
print("Gespeichert in omq_statistik.json! Bleibt für immer!")
