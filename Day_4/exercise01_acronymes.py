# exercise01_acronymes.py

def acronym(phrase: str) -> str:
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words if word)
    return acronym

if __name__ == "__main__":
    test_phrases = [
        "Hyper Text Markup Language",
        "central processing unit",
        "Lomé Tech Community"
    ]
    for phrase in test_phrases:
        print(f"{phrase} → {acronym(phrase)}")
