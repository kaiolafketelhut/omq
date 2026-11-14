import random, json, os

print("=== OMQ - KAI OLAF KETELHUT - BERLIN ===")
print("EAL315 - ALLE SPIELE IN EINEM!\n")

def rate_spiel(max_zahl=100):
    zahl = random.randint(1, max_zahl)
    n = 0
    print(f"Rate 1-{max_zahl}!")
    while True:
        try: tipp = int(input("Dein Tipp: "))
        except: continue
        n += 1
        if tipp < zahl: print("⬆️ ZU KLEIN!")
        elif tipp > zahl: print("⬇️ ZU GROSS!")
        else:
            print(f"🎉 In {n} Versuchen!"); return n

def pc_versuche(zahl):
    low, high, n = 1, 100, 0
    while low <= high:
        tipp = (low+high)//2; n += 1
        if tipp < zahl: low = tipp+1
        elif tipp > zahl: high = tipp-1
        else: return n

while True:
    print("\n--- OMQ MENÜ ---")
    print("1 = EAL310 - Klassik (1-100)")
    print("2 = EAL311 - Du rätst")
    print("3 = EAL312 - Schwierigkeit (1-10 / 1-100 / 1-1000)")
    print("4 = EAL313 - DUELL Du vs PC")
    print("5 = EAL314 - TURNIER Best of 5")
    print("0 = Beenden")
    wahl = input("Wahl: ")
    if wahl == "0":
        print("Danke fürs Spielen! OMQ! 🏆"); break
    elif wahl == "1":
        rate_spiel(100)
    elif wahl == "2":
        rate_spiel(100)
    elif wahl == "3":
        print("1=Leicht 1-10, 2=Mittel 1-100, 3=Schwer 1-1000")
        s = input("Schwierigkeit: ")
        rate_spiel(10 if s=="1" else 1000 if s=="3" else 100)
    elif wahl == "4":
        zahl = random.randint(1,100); n=0
        print("DUELL! Rate 1-100")
        while True:
            tipp=int(input("Dein Tipp: ")); n+=1
            if tipp < zahl: print("⬆️ ZU KLEIN!")
            elif tipp > zahl: print("⬇️ ZU GROSS!")
            else: break
        p = pc_versuche(zahl)
        print(f"DU: {n} - PC: {p} - Zahl: {zahl}")
        print("🏆 DU GEWINNST!" if n<p else "🤖 PC GEWINNT!" if n>p else "🤝 UNENTSCHIEDEN!")
    elif wahl == "5":
        du=pc=0
        while du<3 and pc<3:
            zahl=random.randint(1,100); n=0
            print(f"\nRunde - Stand DU {du}:{pc} PC - Zahl 1-100")
            while True:
                tipp=int(input("Dein Tipp: ")); n+=1
                if tipp < zahl: print("⬆️ ZU KLEIN!")
                elif tipp > zahl: print("⬇️ ZU GROSS!")
                else: break
            p=pc_versuche(zahl)
            print(f"DU {n} - PC {p}")
            if n<p: du+=1; print("🏆 DU gewinnst Runde!")
            elif n>p: pc+=1; print("🤖 PC gewinnt Runde!")
            else: print("🤝 Unentschieden!")
        print(f"🏆 TURNIERSIEGER: DU {du}:{pc}!" if du==3 else f"🤖 TURNIERSIEGER: PC {du}:{pc}!")
    else:
        print("1-5 oder 0 bitte!")
