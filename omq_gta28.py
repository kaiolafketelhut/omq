print("="*42)
print("  OMQ GTA v28 - OMQ ETERNITY 6 ⏳")
print("="*42)
geld = 0
wanted = 0
print("ETERNITY 6! Die Ewigkeit zum 6. Mal! 28. GTA Spiel! Du bist Ewigkeit x6!")
print("1=Eternity-Rennen 2=Eternity-Heist 3=Eternity-Flucht 4=ETERNITY-MISSION 5=Eternity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ ETERNITY 6 > ")
    if w == "1":
        print("⏳ ETERNITY-RENNEN! Du rast durch die Ewigkeit zum 6. Mal!")
        geld += 280000; wanted += 1
    elif w == "2":
        print("⏳ ETERNITY-HEIST! Du klaust die Ewigkeit zum 6. Mal!")
        geld += 290000; wanted += 1
    elif w == "3":
        print("⏳ ETERNITY-FLUCHT! Du entkommst aus der Ewigkeit zum 6. Mal!")
        geld += 300000; wanted += 1
    elif w == "4":
        print("🎯 ETERNITY-MISSION: Die Ewigkeit 6x stehlen! Der Eternity-Coup 6!")
        print("ETERNITY-COUP 6 GESCHAFFT! +3500000$!")
        geld += 3500000; wanted += 3
    elif w == "5":
        print("🔄 Eternity-Reset! Ewigkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE ETERNITY 6 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ETERNITY 6-AUTO | Spiele: 28 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Eternity 6 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Ewigkeit 6! Game Over!")
        print(f"Endstand: {geld}$")
        break
