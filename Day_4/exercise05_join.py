# exercise05_join.py

def join_words(words: list) -> str:
    return " ".join(words)
if __name__ == "__main__":
    listes_de_mots = [
        ["Python", "est", "incroyable"],
        ["Je", "continue", "à", "apprendre"],
        ["Lomé", "a", "des", "talents", "tech"]
    ]

    for mots in listes_de_mots:
        print(f"{mots} → '{join_words(mots)}'")
