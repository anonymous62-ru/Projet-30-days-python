def split_text(text: str) -> list:
    return text.split()

def join_words(words: list) -> str:
    return " ".join(words)

def transform_case(text: str) -> tuple:
    return (text.lower(), text.upper())

def check_start_end(text: str, start: str, end: str) -> tuple:
    return (text.startswith(start), text.endswith(end))

def find_in_text(text: str, sub: str) -> tuple:
    return (text.find(sub), text.index(sub) if sub in text else -1)

def count_occurrence(text: str, word: str) -> int:
    return text.count(word)

def replace_with_dict(text: str, replacements: dict) -> str:
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def check_content(text: str) -> tuple:
    return (text.isnumeric(), text.isalpha())
def convert_types(value: str) -> tuple:
    as_int = int(value)
    as_float = float(value)
    as_str = str(as_int)
    return (as_int, as_float, as_str)

def basic_math(a: float, b: float) -> dict:
    return {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b != 0 else None
    }

def format_number(n: float) -> tuple:
    return (round(n, 2), abs(n))

if __name__ == "__main__":
    # Exemple 1 : chaînes
    print(split_text("Apprendre Python chaque jour"))
    print(join_words(["Apprendre", "Python", "chaque", "jour"]))
    print(transform_case("Coding Remote"))
    print(check_start_end("télétravail motivant", "télé", "ant"))
    print(find_in_text("Je code en Python", "Python"))
    print(count_occurrence("Python est cool. Python est puissant.", "Python"))
    print(replace_with_dict("Python est cool et remote", {"cool": "puissant", "remote": "en télétravail"}))
    print(check_content("123"), check_content("Bonjour"))

    # Exemple 2 : nombres
    print(convert_types("42"))
    print(basic_math(12, 4))
    print(format_number(-8.2579))
