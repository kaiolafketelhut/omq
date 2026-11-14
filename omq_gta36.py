print("="*42)
print("  OMQ GTA v36 - OMQ ETERNITY 10 ⏳")
print("="*42)
geld = 0
wanted = 0
print("ETERNITY 10! Die Ewigkeit zum 10. Mal! ZWEISTELLIG! 36. GTA Spiel! Du bist Ewigkeit x10!")
print("1=Eternity-Rennen 2=Eternity-Heist 3=Eternity-Flucht 4=ETERNITY-MISSION 5=Eternity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ ETERNITY 10 > ")
    if w == "1":
        print("⏳ ETERNITY-RENNEN! Du rast durch die Ewigkeit zum 10. Mal!")
        geld += 470000; wanted += 1
    elif w == "2":
        print("⏳ ETERNITY-HEIST! Du klaust die Ewigkeit zum 10. Mal!")
        geld += 480000; wanted += 1
    elif w == "3":
        print("⏳ ETERNITY-FLUCHT! Du entkommst aus der Ewigkeit zum 10. Mal!")
        geld += 490000; wanted += 1
    elif w == "4":
        print("🎯 ETERNITY-MISSION: Die Ewigkeit 10x stehlen! Der Eternity-Coup 10!")
        print("ETERNITY-COUP 10 GESCHAFFT! +11000000$!")
        geld += 11000000; wanted += 3
    elif w == "5":
        print("🔄 Eternity-Reset! Ewigkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE ETERNITY 10 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ETERNITY 10-AUTO | Spiele: 36 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Eternity 10 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Ewigkeit 10! Game Over!")
        print(f"Endstand: {geld}$")
        break
