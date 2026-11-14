print("="*42)
print("  OMQ GTA v27 - OMQ INFINITY 5 ♾️")
print("="*42)
geld = 0
wanted = 0
print("INFINITY 5! Die Unendlichkeit zum 5. Mal! 27. GTA Spiel! Du bist Unendlichkeit x5!")
print("1=Infinity-Rennen 2=Infinity-Heist 3=Infinity-Flucht 4=INFINITY-MISSION 5=Infinity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ INFINITY 5 > ")
    if w == "1":
        print("♾️ INFINITY-RENNEN! Du rast durch die Unendlichkeit zum 5. Mal!")
        geld += 260000; wanted += 1
    elif w == "2":
        print("♾️ INFINITY-HEIST! Du klaust die Unendlichkeit zum 5. Mal!")
        geld += 270000; wanted += 1
    elif w == "3":
        print("♾️ INFINITY-FLUCHT! Du entkommst aus der Unendlichkeit zum 5. Mal!")
        geld += 280000; wanted += 1
    elif w == "4":
        print("🎯 INFINITY-MISSION: Die Unendlichkeit 5x stehlen! Der Infinity-Coup 5!")
        print("INFINITY-COUP 5 GESCHAFFT! +3000000$!")
        geld += 3000000; wanted += 3
    elif w == "5":
        print("🔄 Infinity-Reset! Unendlichkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE INFINITY 5 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ INFINITY 5-AUTO | Spiele: 27 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Infinity 5 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Unendlichkeit 5! Game Over!")
        print(f"Endstand: {geld}$")
        break
