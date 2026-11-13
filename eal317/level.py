import random, json, os

DATEI = "omq_level.json"

def laden():
    if os.path.exists(DATEI):
        return json.load(open(DATEI))
    return {"xp":0, "level":1, "siege":0, "spiele":0, "titel":"Anfänger"}

def titel_fuer(level):
    if level >= 10: return "👑 OMQ MEISTER"
    if level >= 7: return "🔥 OMQ PROFI"
    if level >= 4: return "⭐ OMQ STAR"
    if level >= 2: return "🎯 OMQ JÄGER"
    return "🌱 Anfänger"

def speichern(s):
    json.dump(s, open(DATEI,"w"), indent=2)

s = laden()
print("=== OMQ EAL317 - LEVEL-UP ===")
print("Kai Olaf Ketelhut - Berlin")
print(f"Level {s['level']} - {s['titel']} - XP: {s['xp']} - Siege: {s['siege']} / Spiele: {s['spiele']}")
print("Gewinn = +50 XP | Unentschieden = +20 XP | Niederlage = +10 XP")
print("Level-Up alle 100 XP!")
print("")

def pc_versuche(zahl):
    low, high, n = 1, 100, 0
    while low <= high:
        tipp=(low+high)//2; n+=1
        if tipp < zahl: low=tipp+1
        elif tipp > zahl: high=tipp-1
        else: return n

zahl = random.randint(1,100); n=0
print("DUELL! Rate 1-100")
while True:
    try: tipp=int(input("Dein Tipp: "))
    except: continue
    n+=1
    if tipp < zahl: print("⬆️ ZU KLEIN!")
    elif tipp > zahl: print("⬇️ ZU GROSS!")
    else: break
p = pc_versuche(zahl)
print(f"DU: {n} - PC: {p} - Zahl: {zahl}")

s["spiele"]+=1
altes_level = s["level"]
if n < p:
    s["siege"]+=1; xp=50; print("🏆 DU GEWINNST! +50 XP!")
elif n == p:
    xp=20; print("🤝 UNENTSCHIEDEN! +20 XP!")
else:
    xp=10; print("🤖 PC GEWINNT! +10 XP fürs Mitspielen!")
s["xp"]+=xp
s["level"] = s["xp"]//100 + 1
s["titel"] = titel_fuer(s["level"])
speichern(s)

print(f"\n=== DEIN FORTSCHRITT ===")
print(f"XP: {s['xp']} | Level: {s['level']} - {s['titel']} | Siege: {s['siege']}/{s['spiele']}")
if s["level"] > altes_level:
    print(f"🎉🎉🎉 LEVEL-UP! Level {altes_level} -> {s['level']} - {s['titel']}!!!")
else:
    print(f"Noch {s['level']*100 - s['xp']} XP bis Level {s['level']+1}!")
print("Gespeichert in omq_level.json!")
