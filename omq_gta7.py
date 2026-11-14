print("="*42)
print("  OMQ GTA v7 - OMQ CITY FINALE 🌆")
print("="*42)
geld = 0
wanted = 0
print("DAS FINALE! Alle Städte in einem! Liberty + Vice + San Andreas!")
print("1=Liberty 2=Vice 3=San Andreas 4=MEGA-MISSION 5=Verstecken 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ CITY FINALE > ")
    if w == "1":
        print("🗽 LIBERTY! Du rast durch Liberty City - Taxi-Chaos!")
        geld += 500; wanted += 1
    elif w == "2":
        print("🌴 VICE! Yacht-Party in Vice City - Sonne, Palmen, Geld!")
        geld += 600; wanted += 1
    elif w == "3":
        print("🏜️ SAN ANDREAS! Wüsten-Rennen - Staub und Vollgas!")
        geld += 700; wanted += 1
    elif w == "4":
        print("🎯 MEGA-MISSION: Alle 3 Städte gleichzeitig ausrauben! Der ultimative Coup!")
        print("MEGA-COUP GESCHAFFT! +10000$!")
        geld += 10000; wanted += 3
    elif w == "5":
        print("🌆 Du versteckst dich im OMQ Tower... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE FINALE === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ GT GOLD | Yacht: OMQ YACHT 2 | Jet: OMQ JET 2 | Alles!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ City Finale verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED im Finale! Game Over!")
        print(f"Endstand: {geld}$")
        break
