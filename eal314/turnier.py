import random

print("=== OMQ EAL314 - TURNIER BEST OF 5 ===")
print("Kai Olaf Ketelhut - Berlin")
print("Wer gewinnt 3 Runden zuerst?")
print("DU vs COMPUTER - Jede Runde neue Zahl 1-100\n")

siege_du = 0
siege_pc = 0
runde = 1

def pc_versuche(zahl):
    low, high = 1, 100
    n = 0
    while low <= high:
        tipp = (low + high)//2
        n += 1
        if tipp < zahl:
            low = tipp + 1
        elif tipp > zahl:
            high = tipp - 1
        else:
            return n

while siege_du < 3 and siege_pc < 3:
    print(f"--- RUNDE {runde} --- Stand: DU {siege_du} : {siege_pc} PC")
    zahl = random.randint(1, 100)
    versuche_du = 0
    while True:
        tipp = int(input("DU - Dein Tipp (1-100): "))
        versuche_du += 1
        if tipp < zahl:
            print("⬆️ ZU KLEIN!")
        elif tipp > zahl:
            print("⬇️ ZU GROSS!")
        else:
            print(f"🎉 DU in {versuche_du} Versuchen!")
            break
    
    versuche_pc = pc_versuche(zahl)
    print(f"🤖 PC braucht {versuche_pc} Versuche (Binary Search) - Zahl war {zahl}")
    
    if versuche_du < versuche_pc:
        print("🏆 DU GEWINNST DIE RUNDE!")
        siege_du += 1
    elif versuche_du > versuche_pc:
        print("🤖 PC GEWINNT DIE RUNDE!")
        siege_pc += 1
    else:
        print("🤝 UNENTSCHIEDEN! Keiner bekommt Punkt!")
    print(f"Stand: DU {siege_du} : {siege_pc} PC\n")
    runde += 1

print("=== TURNIER ENDE ===")
print(f"Endstand: DU {siege_du} : {siege_pc} PC")
if siege_du == 3:
    print("🏆🏆🏆 TURNIERSIEGER: DU! MENSCH SCHLÄGT MASCHINE!")
else:
    print("🤖🤖🤖 TURNIERSIEGER: PC! Maschine ist Champion...")
