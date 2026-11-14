print("="*42)
print("  OMQ GTA v11 - OMQ TIME TRAVEL ⏰")
print("="*42)
geld = 0
wanted = 0
print("ZEITREISE! Dinosaurier + Zukunft + Alles dazwischen!")
print("1=Dino-Zeit 2=Mittelalter 3=Zukunft 4=TIME-MISSION 5=Verstecken 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ TIME TRAVEL > ")
    if w == "1":
        print("🦕 DINO-ZEIT! Du rast vor einem T-Rex weg - Mega-Drift!")
        geld += 3000; wanted += 1
    elif w == "2":
        print("🏰 MITTELALTER! Ritter-Rennen mit Pferden - OMQ Style!")
        geld += 4000; wanted += 1
    elif w == "3":
        print("🤖 ZUKUNFT 3000! Fliegende Autos, Roboter-Polizei - Chaos!")
        geld += 5000; wanted += 1
    elif w == "4":
        print("🎯 TIME-MISSION: Die ganze Zeitlinie gleichzeitig ausrauben! Der Time-Coup!")
        print("TIME-COUP GESCHAFFT! +60000$!")
        geld += 60000; wanted += 3
    elif w == "5":
        print("⏰ Du springst in eine andere Zeit... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE TIME === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ZEITMASCHINE | Dino: OMQ T-REX | Alles!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Time Travel verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Zeit! Game Over!")
        print(f"Endstand: {geld}$")
        break
