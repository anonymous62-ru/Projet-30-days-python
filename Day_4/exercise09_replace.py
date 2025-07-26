# exercise09_replace.py

def replace_words(text: str, old: str, new: str) -> str:
    return text.replace(old, new)
if __name__ == "__main__":
    exemples = [
        ("je veux apprendre python", "python", "le langage Python"),
        ("le code est moche", "moche", "magnifique"),
        ("travailler en présentiel", "présentiel", "remote")
    ]

    for texte, ancien, nouveau in exemples:
        print(f"Avant : '{texte}' → Après : '{replace_words(texte, ancien, nouveau)}'")
