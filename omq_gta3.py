print("="*42)
print("  OMQ GTA v3 - SAN OMQ ANDREAS 🏜️")
print("="*42)
geld = 0
wanted = 0
print("3 Städte! Los Santos, San Fierro, Las Venturas!")
print("1=Auto 2=Zug 3=Jetpack 4=Mission 5=Verstecken 6=Stadt wechseln 0=Aussteigen")
stadt = "Los Santos"
while True:
    w = input(f"\n[{stadt}] SAN OMQ > ")
    if w == "1":
        print("🚗 Du fährst durch Los Santos... Gangster-Style!")
        geld += 150; wanted += 1
    elif w == "2":
        print("🚂 ZUG-MISSION! Du fährst auf dem Zug! CJ Style!")
        geld += 400; wanted += 1
    elif w == "3":
        print("🚀 JETPACK! Du fliegst über ganz San Andreas! WOW!")
        geld += 600; wanted += 2
    elif w == "4":
        print("🎯 MISSION: Casino in Las Venturas ausrauben!")
        print("JACKPOT! +2000$!")
        geld += 2000; wanted += 3
    elif w == "5":
        print("🏠 Du versteckst dich im Safehouse... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        if stadt == "Los Santos": stadt = "San Fierro"
        elif stadt == "San Fierro": stadt = "Las Venturas"
        else: stadt = "Los Santos"
        print(f"✈️ Du fliegst nach {stadt}!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in San Andreas verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted} | Stadt: {stadt}")
    if wanted >= 6:
        print("\n💥 BUSTED in San Andreas! Game Over!")
        print(f"Endstand: {geld}$")
        break
