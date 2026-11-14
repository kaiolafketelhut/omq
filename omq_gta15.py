print("="*42)
print("  OMQ GTA v15 - OMQ LEGEND 🌟")
print("="*42)
geld = 0
wanted = 0
print("LEGENDE! Das allerletzte GTA! Du bist die Legende von OMQ!")
print("1=Legenden-Rennen 2=Legenden-Heist 3=Legenden-Flucht 4=LEGEND-MISSION 5=Legenden-Pause 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ LEGEND > ")
    if w == "1":
        print("🌟 LEGENDEN-RENNEN! Alle kennen deinen Namen - alle jubeln dir zu!")
        geld += 25000; wanted += 1
    elif w == "2":
        print("🌟 LEGENDEN-HEIST! Der größte Heist aller Zeiten - nur du kannst das!")
        geld += 30000; wanted += 1
    elif w == "3":
        print("🌟 LEGENDEN-FLUCHT! Du entkommst - weil du eine LEGENDE bist!")
        geld += 35000; wanted += 1
    elif w == "4":
        print("🎯 LEGEND-MISSION: Das letzte Imperium stehlen! Der Legend-Coup!")
        print("LEGEND-COUP GESCHAFFT! +300000$!")
        geld += 300000; wanted += 3
    elif w == "5":
        print("👑 Legenden-Pause! Du ruhst dich aus - wie ein König!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE LEGEND === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ LEGEND-AUTO | Titel: OMQ LEGENDE!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Legend verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED als Legende! Game Over!")
        print(f"Endstand: {geld}$")
        break
