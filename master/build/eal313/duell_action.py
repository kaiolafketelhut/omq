import os, random
deine = int(os.environ.get("INPUT_DEINE_VERSUCHE", "10"))
# PC braucht max 7 für 1-100 mit Binary Search
pc = random.randint(5, 7)
print(f"=== EAL313 DUELL ===")
print(f"DU: {deine} Versuche")
print(f"PC: {pc} Versuche (Binary Search)")
if deine < pc:
    print("🏆 DU GEWINNST! MENSCH SCHLÄGT MASCHINE!")
elif deine > pc:
    print("🤖 PC GEWINNT!")
else:
    print("🤝 UNENTSCHIEDEN!")
