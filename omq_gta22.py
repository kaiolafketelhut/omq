print("="*42)
print("  OMQ GTA v22 - OMQ ETERNITY 3 ⏳")
print("="*42)
geld = 0
wanted = 0
print("ETERNITY 3! Die Ewigkeit zum 3. Mal! 22. GTA Spiel! Du bist Ewigkeit x3!")
print("1=Eternity-Rennen 2=Eternity-Heist 3=Eternity-Flucht 4=ETERNITY-MISSION 5=Eternity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ ETERNITY 3 > ")
    if w == "1":
        print("⏳ ETERNITY-RENNEN! Du rast durch die Ewigkeit zum 3. Mal!")
        geld += 150000; wanted += 1
    elif w == "2":
        print("⏳ ETERNITY-HEIST! Du klaust die Ewigkeit zum 3. Mal!")
        geld += 160000; wanted += 1
    elif w == "3":
        print("⏳ ETERNITY-FLUCHT! Du entkommst aus der Ewigkeit zum 3. Mal!")
        geld += 170000; wanted += 1
    elif w == "4":
        print("🎯 ETERNITY-MISSION: Die Ewigkeit 3x stehlen! Der Eternity-Coup 3!")
        print("ETERNITY-COUP 3 GESCHAFFT! +1000000$!")
        geld += 1000000; wanted += 3
    elif w == "5":
        print("🔄 Eternity-Reset! Ewigkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE ETERNITY 3 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ETERNITY 3-AUTO | Spiele: 22 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Eternity 3 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Ewigkeit 3! Game Over!")
        print(f"Endstand: {geld}$")
        break
