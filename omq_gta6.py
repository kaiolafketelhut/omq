print("="*42)
print("  OMQ GTA v6 - SAN ANDREAS 2 🏜️")
print("="*42)
geld = 0
wanted = 0
print("Zurück in San Andreas! Wüste, Fallschirm, Casino!")
print("1=Wüste 2=Fallschirm 3=BMX 4=Mission 5=Verstecken 6=Garage 0=Aussteigen")
while True:
    w = input("\nSAN ANDREAS 2 > ")
    if w == "1":
        print("🏜️ WÜSTEN-RENNEN! Du rast durch die Wüste - Staub überall!")
        geld += 350; wanted += 1
    elif w == "2":
        print("🪂 FALLSCHIRM! Du springst aus dem Flugzeug über San Andreas!")
        geld += 700; wanted += 1
    elif w == "3":
        print("🚲 BMX-TRICKS! Du machst Backflips auf deinem BMX!")
        geld += 300; wanted += 0
    elif w == "4":
        print("🎯 MISSION: Casino in Las Venturas ausrauben! Der große Coup!")
        print("CASINO GEKNACKT! +5000$!")
        geld += 5000; wanted += 3
    elif w == "5":
        print("🏜️ Du versteckst dich in der Wüste... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE SAN 2 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ GT GOLD | BMX: OMQ BMX PRO | Flugzeug: OMQ JET 2")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in San Andreas 2 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in San Andreas 2! Game Over!")
        print(f"Endstand: {geld}$")
        break
