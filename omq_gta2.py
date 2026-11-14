print("="*42)
print("  OMQ GTA v2 - VICE OMQ CITY 🌴")
print("="*42)
geld = 0
wanted = 0
print("Willkommen in Vice OMQ City! Sonne, Strand, Chaos!")
print("1=Auto  2=Boot  3=Heli  4=Mission  5=Verstecken  6=Garage  0=Aussteigen")

while True:
    w = input("\nVICE OMQ > ")
    if w == "1":
        print("🚗 Du cruist am Strand entlang... 🌴")
        geld += 100; wanted += 1
    elif w == "2":
        print("🛥️ Du fährst mit dem Boot übers Meer... Wellen!")
        geld += 200; wanted += 1
    elif w == "3":
        print("🚁 Du fliegst mit dem Heli über die Stadt! WOW!")
        geld += 300; wanted += 2
    elif w == "4":
        print("🎯 MISSION: Bank in Vice City! Schnell weg!")
        print("Mission geschafft! +1000$!")
        geld += 1000; wanted += 2
    elif w == "5":
        print("🏖️ Du versteckst dich am Strand... Keiner findet dich!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE VICE === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ GT GOLD | Boot: OMQ YACHT | Heli: OMQ COPTER")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in Vice City verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in Vice City! 6 Sterne! Game Over!")
        print(f"Endstand: {geld}$")
        break
