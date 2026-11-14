print("="*42)
print("  OMQ GTA v20 - OMQ ETERNITY 2 ♾️")
print("="*42)
geld = 0
wanted = 0
print("ETERNITY 2! 20. GTA Spiel! Die Ewigkeit zum 2. Mal! Du bist Ewig x2!")
print("1=Eternity-Rennen 2=Eternity-Heist 3=Eternity-Flucht 4=ETERNITY-MISSION 5=Eternity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ ETERNITY 2 > ")
    if w == "1":
        print("♾️ ETERNITY-RENNEN! Du rast durch die Ewigkeit zum 2. Mal!")
        geld += 120000; wanted += 1
    elif w == "2":
        print("♾️ ETERNITY-HEIST! Du klaust die Ewigkeit zum 2. Mal!")
        geld += 130000; wanted += 1
    elif w == "3":
        print("♾️ ETERNITY-FLUCHT! Du entkommst aus der Ewigkeit zum 2. Mal!")
        geld += 140000; wanted += 1
    elif w == "4":
        print("🎯 ETERNITY-MISSION: Die Ewigkeit 2x stehlen! Der Eternity-Coup 2!")
        print("ETERNITY-COUP 2 GESCHAFFT! +800000$!")
        geld += 800000; wanted += 3
    elif w == "5":
        print("🔄 Eternity-Reset! Ewigkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE ETERNITY 2 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ETERNITY 2-AUTO | Spiele: 20 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Eternity 2 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Ewigkeit 2! Game Over!")
        print(f"Endstand: {geld}$")
        break
