import math

# 1️⃣ Somme de deux nombres
def add_two_numbers(a, b):
    return a + b

# 2️⃣ Aire d’un cercle
def area_of_circle(r):
    return math.pi * r * r

# 3️⃣ Addition de plusieurs nombres (avec vérification)
def add_all_nums(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    else:
        return "❌ Tous les éléments doivent être des nombres."

# 4️⃣ Conversion Celsius → Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 5️⃣ Vérification de la saison selon le mois
def check_season(month):
    mois = month.lower()
    saisons = {
        "décembre": "hiver", "janvier": "hiver", "février": "hiver",
        "mars": "printemps", "avril": "printemps", "mai": "printemps",
        "juin": "été", "juillet": "été", "août": "été",
        "septembre": "automne", "octobre": "automne", "novembre": "automne"
    }
    return saisons.get(mois, "❓ Mois inconnu")

# 6️⃣ Calcul de la pente (slope = dy/dx)
def calcul_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "⚠️ Division par zéro (droite verticale)"
    return (y2 - y1) / (x2 - x1)

# 7️⃣ Résolution d’équation quadratique
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "⚠️ Pas de solution réelle"
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return x1, x2

# 8️⃣ Impression d’une liste
def print_list(lst):
    for item in lst:
        print(item)

# 9️⃣ Inversion d’une liste avec boucle
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# 🔟 Capitalisation des éléments d’une liste
def capitalize_list_items(lst):
    return [str(item).upper() for item in lst]

# 1️⃣1️⃣ Ajouter un élément à la fin
def add_item(lst, item):
    lst.append(item)
    return lst

# 1️⃣2️⃣ Supprimer un élément
def remove_item(lst, item):
    return [x for x in lst if x != item]

# 1️⃣3️⃣ Somme d’une plage de nombres
def sum_of_numbers(n):
    return sum(range(n + 1))

# 1️⃣4️⃣ Somme des nombres impairs
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# 1️⃣5️⃣ Somme des nombres pairs
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
