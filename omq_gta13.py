print("="*42)
print("  OMQ GTA v13 - OMQ UNDERWORLD 👹")
print("="*42)
geld = 0
wanted = 0
print("UNTERWELT! Hölle + Himmel + Geister! Du klaust sogar im Jenseits!")
print("1=Höllen-Rennen 2=Himmel-Heist 3=Geister-Flucht 4=UNDER-MISSION 5=Verstecken 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ UNDERWORLD > ")
    if w == "1":
        print("🔥 HÖLLEN-RENNEN! Du rast durch Lava - mit dem Teufel als Beifahrer!")
        geld += 8000; wanted += 1
    elif w == "2":
        print("😇 HIMMEL-HEIST! Du klaust den Engeln ihre goldenen Autos!")
        geld += 10000; wanted += 1
    elif w == "3":
        print("👻 GEISTER-FLUCHT! Du bist unsichtbar - Geister-Polizei jagt dich!")
        geld += 12000; wanted += 1
    elif w == "4":
        print("🎯 UNDER-MISSION: Die ganze Unterwelt gleichzeitig ausrauben! Der Under-Coup!")
        print("UNDER-COUP GESCHAFFT! +130000$!")
        geld += 130000; wanted += 3
    elif w == "5":
        print("🙏 Du versteckst dich in einer Kirche... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE UNDER === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ HÖLLEN-AUTO | Flügel: OMQ ENGEL | Alles!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Underworld verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Unterwelt! Game Over!")
        print(f"Endstand: {geld}$")
        break
