import random, json, os
DATEI="omq_abzeichen.json"
def laden():
    if os.path.exists(DATEI): return json.load(open(DATEI))
    return {"spiele":0,"siege":0,"serie":0,"best":99,"abzeichen":[]}
def speichern(s): json.dump(s, open(DATEI,"w"), indent=2)
s=laden()
print("=== OMQ EAL318 - ABZEICHEN ===")
print(f"Spiele: {s['spiele']} | Siege: {s['siege']} | Beste Serie: {s['serie']} | Best: {s['best']}")
print(f"Deine Abzeichen: {', '.join(s['abzeichen']) if s['abzeichen'] else 'Noch keine - hol sie dir!'}")
print("")
def pc(zahl):
    lo,hi,n=1,100,0
    while lo<=hi:
        t=(lo+hi)//2; n+=1
        if t<zahl: lo=t+1
        elif t>zahl: hi=t-1
        else: return n
zahl=random.randint(1,100); n=0
print("DUELL! Rate 1-100")
while True:
    try: t=int(input("Dein Tipp: "))
    except: continue
    n+=1
    if t<zahl: print("⬆️ ZU KLEIN!")
    elif t>zahl: print("⬇️ ZU GROSS!")
    else: break
p=pc(zahl)
print(f"DU: {n} - PC: {p} - Zahl: {zahl}")
s["spiele"]+=1
neu=[]
if n<p:
    s["siege"]+=1; s["serie"]+=1; print("🏆 DU GEWINNST!")
    if "🎯 Erster Sieg" not in s["abzeichen"]: neu.append("🎯 Erster Sieg")
else:
    s["serie"]=0
    print("🤖 PC GEWINNT!" if n>p else "🤝 UNENTSCHIEDEN!")
if n<99 and n<s["best"]: s["best"]=n
if n<=5 and "⚡ Blitz-Sieg" not in s["abzeichen"] and n<p: neu.append("⚡ Blitz-Sieg (unter 5!)")
if s["serie"]>=3 and "🔥 3er-Serie" not in s["abzeichen"]: neu.append("🔥 3er-Serie!")
if s["siege"]>=5 and "⭐ 5 Siege" not in s["abzeichen"]: neu.append("⭐ 5 Siege!")
if s["spiele"]>=10 and "🎮 10 Spiele" not in s["abzeichen"]: neu.append("🎮 10 Spiele!")
for a in neu:
    if a not in s["abzeichen"]: s["abzeichen"].append(a)
    print(f"🎉 NEUES ABZEICHEN: {a}!!!")
speichern(s)
print(f"\n=== DEINE ABZEICHEN ({len(s['abzeichen'])}/5) ===")
for a in s["abzeichen"]: print(f" - {a}")
print("Gespeichert!")
