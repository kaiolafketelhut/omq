print("="*42)
print("  OMQ GTA v4 - LIBERTY OMQ CITY 2 🗽")
print("="*42)
geld = 0
wanted = 0
print("Zurück in Liberty! Taxi, U-Bahn, Verfolgung!")
print("1=Taxi 2=U-Bahn 3=Heli-Verfolgung 4=Mission 5=Verstecken 6=Garage 0=Aussteigen")
while True:
    w = input("\nLIBERTY 2 > ")
    if w == "1":
        print("🚕 TAXI-MISSION! Du bringst einen Fahrgast quer durch die Stadt!")
        geld += 250; wanted += 1
    elif w == "2":
        print("🚇 Du fährst mit der U-Bahn unter der Stadt durch... Schnell!")
        geld += 200; wanted += 0
    elif w == "3":
        print("🚁 HELI-VERFOLGUNG! Polizei-Heli hinter dir! Vollgas!")
        geld += 500; wanted += 2
    elif w == "4":
        print("🎯 MISSION: Juwelier in Liberty City ausrauben! Diamanten!")
        print("DIAMANTEN! +3000$!")
        geld += 3000; wanted += 3
    elif w == "5":
        print("🏢 Du versteckst dich in einem Parkhaus... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE LIBERTY 2 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ GT GOLD | Taxi: OMQ CAB | Heli: OMQ COPTER 2")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in Liberty 2 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in Liberty 2! Game Over!")
        print(f"Endstand: {geld}$")
        break
