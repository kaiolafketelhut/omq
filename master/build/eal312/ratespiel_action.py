import os
level = os.environ.get("INPUT_SCHWIERIGKEIT", "mittel").lower()
tipp = int(os.environ.get("INPUT_TIPP", "50"))
geheim = int(os.environ.get("INPUT_GEHEIMZAHL", "42"))
max_zahl = {"leicht": 10, "schwer": 1000}.get(level, 100)
print(f"=== EAL312 - Level {level.upper()} 1-{max_zahl} ===")
print(f"Dein Tipp: {tipp}")
if tipp < geheim:
    print("⬆️ ZU KLEIN! Höher!")
elif tipp > geheim:
    print("⬇️ ZU GROSS! Tiefer!")
else:
    print("🎉 RICHTIG! 🏆 Highscore!")
