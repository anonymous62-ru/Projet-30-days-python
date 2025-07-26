# exercise03_remplacement.py

def custom_replace(text: str, old: str, new: str) -> str:
    return text.replace(old, new)

if __name__ == "__main__":
    print(custom_replace("Je suis un développeur Python", "Python", "Rust"))
    print(custom_replace("Salut le monde, le monde est beau", "monde", "univers"))
    print(custom_replace("Lomé est une ville", "ville", "capitale"))
