# exercise06_strip.py

def clean_text(raw_text: str) -> str:
    return raw_text.strip()
if __name__ == "__main__":
    exemples = [
        "   Je veux créer une app mobile   ",
        "\tMotivé pour le remote work\n",
        "   #ApprendrePython     "
    ]

    for texte in exemples:
        print(f"Avant : '{texte}' → Après : '{clean_text(texte)}'")
