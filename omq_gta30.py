print("="*42)
print("  OMQ GTA v30 - OMQ ETERNITY 7 ⏳")
print("="*42)
geld = 0
wanted = 0
print("ETERNITY 7! Die Ewigkeit zum 7. Mal! 30. GTA Spiel! Du bist Ewigkeit x7!")
print("1=Eternity-Rennen 2=Eternity-Heist 3=Eternity-Flucht 4=ETERNITY-MISSION 5=Eternity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ ETERNITY 7 > ")
    if w == "1":
        print("⏳ ETERNITY-RENNEN! Du rast durch die Ewigkeit zum 7. Mal!")
        geld += 320000; wanted += 1
    elif w == "2":
        print("⏳ ETERNITY-HEIST! Du klaust die Ewigkeit zum 7. Mal!")
        geld += 330000; wanted += 1
    elif w == "3":
        print("⏳ ETERNITY-FLUCHT! Du entkommst aus der Ewigkeit zum 7. Mal!")
        geld += 340000; wanted += 1
    elif w == "4":
        print("🎯 ETERNITY-MISSION: Die Ewigkeit 7x stehlen! Der Eternity-Coup 7!")
        print("ETERNITY-COUP 7 GESCHAFFT! +5000000$!")
        geld += 5000000; wanted += 3
    elif w == "5":
        print("🔄 Eternity-Reset! Ewigkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE ETERNITY 7 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ETERNITY 7-AUTO | Spiele: 30 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Eternity 7 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Ewigkeit 7! Game Over!")
        print(f"Endstand: {geld}$")
        break
