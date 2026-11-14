import random, getpass
print("=== OMQ EAL321 - 2 SPIELER ===")
print("Spieler 1 denkt sich Zahl aus, Spieler 2 raet!")
try:
    geheim = getpass.getpass("Spieler 1 - Geheime Zahl 1-100 (Enter=Zufall): ")
    zahl = int(geheim) if geheim.strip() else random.randint(1,100)
except: zahl = random.randint(1,100)
print("\n"*30)
print("Spieler 2 - Jetzt raten!")
n=0
while True:
    try: t=int(input("Dein Tipp: "))
    except: continue
    n+=1
    if t<zahl: print("ZU KLEIN!")
    elif t>zahl: print("ZU GROSS!")
    else: break
print(f"GESCHAFFT in {n} Versuchen! Zahl: {zahl}")
