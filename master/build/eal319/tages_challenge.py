import random, json, os, datetime
HEUTE = datetime.date.today().isoformat()
DATEI = "omq_tages.json"
def laden():
    if os.path.exists(DATEI): return json.load(open(DATEI))
    return {"letzter_tag":"","streak":0,"gespielt":0,"gewinne":0}
def speichern(s): json.dump(s, open(DATEI,"w"), indent=2)
s = laden()
# Zahl ist jeden Tag gleich - Seed = Datum!
random.seed(HEUTE)
zahl = random.randint(1,100)
print("=== OMQ EAL319 - TAGES-CHALLENGE ===")
print(f"Datum: {HEUTE}")
print(f"Dein Streak: {s['streak']} Tage | Gespielt: {s['gespielt']} | Siege: {s['gewinne']}")
if s["letzter_tag"] == HEUTE:
    print("⚠️ Heute schon gespielt! Komm morgen wieder für neuen Streak!")
else:
    print("🔥 NEUE TAGES-ZAHL! Alle Spieler haben heute die gleiche Zahl!")
print("")
def pc(zahl):
    lo,hi,n=1,100,0
    while lo<=hi:
        t=(lo+hi)//2; n+=1
        if t<zahl: lo=t+1
        elif t>zahl: hi=t-1
        else: return n
n=0
print("DUELL! Rate 1-100 - Du hast max. 7 Versuche!")
while n < 7:
    try: t=int(input("Dein Tipp: "))
    except: continue
    n+=1
    if t<zahl: print("⬆️ ZU KLEIN!")
    elif t>zahl: print("⬇️ ZU GROSS!")
    else: break
p=pc(zahl)
print(f"DU: {n} - PC: {p} - Zahl: {zahl}")
if n<=7 and t==zahl:
    print("🏆 TAGES-CHALLENGE GESCHAFFT!")
    if s["letzter_tag"] != HEUTE:
        s["gespielt"]+=1
        if n < p:
            s["gewinne"]+=1; s["streak"]+=1
            print(f"🔥 STREAK: {s['streak']} Tage in Folge! Du schlägst den PC!")
        else:
            s["streak"]=0
            print("PC war schneller, Streak zurückgesetzt!")
        s["letzter_tag"]=HEUTE
        speichern(s)
else:
    print("💥 7 Versuche vorbei! Morgen neue Chance!")
    if s["letzter_tag"] != HEUTE:
        s["gespielt"]+=1; s["streak"]=0; s["letzter_tag"]=HEUTE
        speichern(s)
print(f"\nStreak: {s['streak']} | Siege: {s['gewinne']}/{s['gespielt']}")
print("Gespeichert! Morgen gibt es eine neue Zahl!")
