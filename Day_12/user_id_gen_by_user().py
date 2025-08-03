def user_id_gen_by_user():
    import random
    import string

    longueur = int(input("Nombre de caractères : "))
    nombre = int(input("Nombre d'IDs à générer : "))
    characters = string.ascii_lowercase + string.digits
    ids = ['#' + ''.join(random.choices(characters, k=longueur)) for _ in range(nombre)]
    return ' '.join(ids)

print(user_id_gen_by_user())
