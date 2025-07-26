# exercise04_split.py

def split_sentence(sentence: str) -> list:
    return sentence.split()

if __name__ == "__main__":
    phrases = [
        "Python est un langage puissant",
        "Développeur à Lomé motivé et structuré",
        "Apprendre chaque jour, progresser chaque semaine"
    ]

    for phrase in phrases:
        print(f"{phrase} → {split_sentence(phrase)}")
