# Fonctions centralisées pour récupérer les saisies utilisateur

def get_float(prompt):
    return float(input(prompt))

def get_triangle_base_height():
    base = get_float("Entrez la base du triangle : ")
    height = get_float("Entrez la hauteur du triangle : ")
    return base, height

def get_triangle_sides():
    a = get_float("Côté A : ")
    b = get_float("Côté B : ")
    c = get_float("Côté C : ")
    return a, b, c

def get_rectangle_dimensions():
    length = get_float("Longueur du rectangle : ")
    width = get_float("Largeur du rectangle : ")
    return length, width

def get_circle_radius():
    return get_float("Rayon du cercle : ")

def get_mass_and_volume():
    mass = get_float("Masse en kg : ")
    volume = get_float("Volume en m³ : ")
    return mass, volume

def get_x_for_equation(prompt="Valeur de x : "):
    return get_float(prompt)


from user_inputs import get_triangle_base_height, get_x_for_equation
