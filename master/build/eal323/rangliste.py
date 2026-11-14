import json, os, random, time
print("=== OMQ EAL323 - RANGLISTE ===")
print("Deine besten Spiele - fuer immer gespeichert!")
print("")

DATEI = "eal323/rangliste.json"

# Alte Rangliste laden
if os.path.exists(DATEI):
    with open(DATEI) as f:
        liste = json.load(f)
else:
    liste = [{"name": "Kai", "score": 599, "zeit": 26.1, "versuche": 7}]

# Neues Spiel - Speed-Run
print("--- Neues Spiel ---")
zahl = random.randint(1,100)
versuche = 0
start = time.time()
while True:
    try: t = int(input("Tipp 1-100: "))
    except: continue
    versuche += 1
    if t < zahl: print("ZU KLEIN!")
    elif t > zahl: print("ZU GROSS!")
    else: break
dauer = round(time.time()-start, 1)
score = max(0, 1000 - int(dauer*10) - versuche*20)
print(f"\nGESCHAFFT! Zahl {zahl} | {versuche} Versuche | {dauer}s | Score {score}")

name = input("Dein Name: ") or "Kai"
liste.append({"name": name, "score": score, "zeit": dauer, "versuche": versuche})
liste = sorted(liste, key=lambda x: x["score"], reverse=True)[:5]

with open(DATEI, "w") as f:
    json.dump(liste, f, indent=2)

print("\n=== 🏆 OMQ TOP 5 RANGLISTE ===")
for i, e in enumerate(liste, 1):
    medaille = ["🥇","🥈","🥉","4.","5."][i-1]
    print(f"{medaille} {e['name']} - {e['score']} Punkte ({e['versuche']} Versuche, {e['zeit']}s)")
