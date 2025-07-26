# exercise02_formatage.py

def greet_user(name: str, age: int) -> str:
    f_string_message = f"Bonjour {name}, tu as {age} ans."

    format_message = "Bonjour {}, tu as {} ans.".format(name, age)

    return f_string_message + "\n" + format_message

if __name__ == "__main__":
    print(greet_user("Amèvi", 30))
    print(greet_user("Maxime", 25))
