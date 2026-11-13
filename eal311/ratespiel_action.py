import os
tipp = int(os.environ.get("INPUT_TIPP", "50"))
geheim = int(os.environ.get("INPUT_GEHEIMZAHL", "42"))
print(f"=== EAL311 - Dein Tipp: {tipp} ===")
if tipp < geheim:
    print("⬆️ ZU KLEIN! Höher!")
elif tipp > geheim:
    print("⬇️ ZU GROSS! Tiefer!")
else:
    print("🎉 RICHTIG!")
