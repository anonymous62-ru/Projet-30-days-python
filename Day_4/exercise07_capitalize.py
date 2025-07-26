# exercise07_capitalize.py

def format_text(text: str) -> str:
    return text.capitalize()
if __name__ == "__main__":
    exemples = [
        "bonjour tout le MONDE",
        "J'AIME le PYTHON",
        "remote WORK est motivant"
    ]

    for phrase in exemples:
        print(f"Avant : '{phrase}' → Après : '{format_text(phrase)}'")
