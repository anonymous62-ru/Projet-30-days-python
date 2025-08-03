import random
import string

def random_user_id():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=6))

def user_id_gen_by_user():
    try:
        longueur = int(input("Nombre de caractères : "))
        nombre = int(input("Nombre d'IDs à générer : "))
        characters = string.ascii_lowercase + string.digits
        ids = ['#' + ''.join(random.choices(characters, k=longueur)) for _ in range(nombre)]
        return ' '.join(ids)
    except ValueError:
        return "⚠️ Entrée invalide. Merci de saisir uniquement des nombres."

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"RGB({r}, {g}, {b})"


# 🔎 Test rapide des trois fonctions
if __name__ == "__main__":
    print("▶ ID aléatoire (6 caractères) :", random_user_id())
    print("▶ Générateur d'IDs personnalisés :", user_id_gen_by_user())
    print("▶ Couleur RGB générée :", rgb_color_gen())
