# Jour 2: 30 Days of Python Programming - Niveau 2

# Déclaration initiale
first_name = "Maxime"
last_name = "Amèvi"
country = "Togo"
age = 28
is_married = False

# 1. Vérification des types
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))
print(type(is_married))

# 2. Longueur du prénom
print("Longueur du prénom :", len(first_name))

# 3. Comparaison des longueurs
print("Le prénom est plus long que le nom ?", len(first_name) > len(last_name))

# 4. Déclaration des nombres
num_one = 5
num_two = 4

# 5-10. Opérations mathématiques
total = num_one + num_two
print("Addition :", total)

diff = num_one - num_two
print("Soustraction :", diff)

product = num_one * num_two
print("Multiplication :", product)

division = num_one / num_two
print("Division :", division)

remainder = num_one % num_two
print("Reste :", remainder)

floor_division = num_one // num_two
print("Division entière :", floor_division)

# 12. Calcul sur un cercle avec rayon = 30
radius = 30
pi = 3.1416

area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Aire du cercle :", area_of_circle)
print("Circonférence :", circum_of_circle)

# iii. Entrée utilisateur pour calculer aire
user_radius = float(input("Entrez le rayon du cercle : "))
user_area = pi * user_radius ** 2
print("Aire pour le rayon entré :", user_area)

# 13. Saisie d'informations utilisateur
user_first_name = input("Quel est votre prénom ? ")
user_last_name = input("Quel est votre nom de famille ? ")
user_country = input("Quel est votre pays ? ")
user_age = input("Quel est votre âge ? ")

print("Infos utilisateur:", user_first_name, user_last_name, user_country, user_age)

# 14. Vérification des mots-clés Python
help("keywords")
