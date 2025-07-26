# exercise08_title.py

def format_as_title(text: str) -> str:
    return text.title()
if __name__ == "__main__":
    exemples = [
        "mon projet python avance bien",
        "la discipline mène au succès",
        "partager son code sur github"
    ]

    for phrase in exemples:
        print(f"Avant : '{phrase}' → Après : '{format_as_title(phrase)}'")
