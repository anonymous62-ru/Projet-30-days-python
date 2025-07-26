def format_scientific(n: float) -> str:
    return f"{n:.2e}"

def safe_division(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf")

def random_int_range(start: int, end: int) -> int:
    from random import randint
    return randint(start, end)

def is_even(n: int) -> bool:
    return n % 2 == 0

def is_positive(n: float) -> bool:
    return n > 0

def logical_combine(a: bool, b: bool) -> dict:
    return {
        "and": a and b,
        "or": a or b,
        "not a": not a,
        "not b": not b
    }

def safe_input_to_int(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        return None

def create_acronym(phrase: str) -> str:
    return ''.join(word[0].upper() for word in phrase.split())

def clean_and_format(text: str) -> str:
    cleaned = text.strip()
    formatted = cleaned.title()
    return formatted.replace("Remote", "Télétravail")

if __name__ == "__main__":
    print(format_scientific(34566))
    print(safe_division(10, 0))
    print(random_int_range(1, 100))
    print(is_even(8), is_positive(-3))
    print(logical_combine(True, False))
    print(safe_input_to_int("42"))
    print(safe_input_to_int("hello"))

    print(create_acronym("Learning Python Language"))
    print(clean_and_format("   le remote work avec Python   "))
