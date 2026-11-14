print("="*42)
print("  OMQ GTA v23 - OMQ INFINITY 3 ♾️")
print("="*42)
geld = 0
wanted = 0
print("INFINITY 3! Die Unendlichkeit zum 3. Mal! 23. GTA Spiel! Du bist Unendlichkeit x3!")
print("1=Infinity-Rennen 2=Infinity-Heist 3=Infinity-Flucht 4=INFINITY-MISSION 5=Infinity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ INFINITY 3 > ")
    if w == "1":
        print("♾️ INFINITY-RENNEN! Du rast durch die Unendlichkeit zum 3. Mal!")
        geld += 180000; wanted += 1
    elif w == "2":
        print("♾️ INFINITY-HEIST! Du klaust die Unendlichkeit zum 3. Mal!")
        geld += 190000; wanted += 1
    elif w == "3":
        print("♾️ INFINITY-FLUCHT! Du entkommst aus der Unendlichkeit zum 3. Mal!")
        geld += 200000; wanted += 1
    elif w == "4":
        print("🎯 INFINITY-MISSION: Die Unendlichkeit 3x stehlen! Der Infinity-Coup 3!")
        print("INFINITY-COUP 3 GESCHAFFT! +1250000$!")
        geld += 1250000; wanted += 3
    elif w == "5":
        print("🔄 Infinity-Reset! Unendlichkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE INFINITY 3 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ INFINITY 3-AUTO | Spiele: 23 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Infinity 3 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Unendlichkeit 3! Game Over!")
        print(f"Endstand: {geld}$")
        break
