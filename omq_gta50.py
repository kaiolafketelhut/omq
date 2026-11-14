print("="*42)
print("  OMQ GTA v50 - OMQ ETERNITY 17 ⏳")
print("="*42)
geld = 0
wanted = 0
print("ETERNITY 17! Die Ewigkeit zum 17. Mal! 50. GTA Spiel! JUBILÄUM! Du bist Ewigkeit x17!")
print("1=Eternity-Rennen 2=Eternity-Heist 3=Eternity-Flucht 4=ETERNITY-MISSION 5=Eternity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ ETERNITY 17 > ")
    if w == "1":
        print("⏳ ETERNITY-RENNEN! Du rast durch die Ewigkeit zum 17. Mal!")
        geld += 890000; wanted += 1
    elif w == "2":
        print("⏳ ETERNITY-HEIST! Du klaust die Ewigkeit zum 17. Mal!")
        geld += 900000; wanted += 1
    elif w == "3":
        print("⏳ ETERNITY-FLUCHT! Du entkommst aus der Ewigkeit zum 17. Mal!")
        geld += 910000; wanted += 1
    elif w == "4":
        print("🎯 ETERNITY-MISSION: Die Ewigkeit 17x stehlen! Der Eternity-Coup 17!")
        print("ETERNITY-COUP 17 GESCHAFFT! +25000000$!")
        geld += 25000000; wanted += 3
    elif w == "5":
        print("🔄 Eternity-Reset! Ewigkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE ETERNITY 17 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ETERNITY 17-AUTO | Spiele: 50 GTA Spiele! JUBILÄUM!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Eternity 17 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Ewigkeit 17! Game Over!")
        print(f"Endstand: {geld}$")
        break
