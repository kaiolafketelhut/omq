import os, random
deine = int(os.environ.get("INPUT_DEINE_SIEGE", "3"))
pc = 3 - deine if deine < 3 else random.randint(0, 2)
print(f"=== EAL314 TURNIER ===")
print(f"DU: {deine} Siege - PC: {pc} Siege")
if deine == 3:
    print("🏆 TURNIERSIEGER: DU!")
else:
    print("🤖 TURNIERSIEGER: PC!")
