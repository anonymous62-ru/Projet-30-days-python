# Exo 1. Créer un tuple vide
empty_tuple = ()
print("Tuple vide:", empty_tuple)

# Exo 2. Créer un tuple avec frères et sœurs imaginaires
brothers = ("Kodjo", "Yaw", "Kossi")
sisters = ("Akou", "Dede", "Afi")
print("Frères:", brothers)
print("Sœurs:", sisters)

# Exo 3. Rejoindre les tuples
siblings = brothers + sisters
print("Fratrie:", siblings)

# Exo 4. Compter le nombre de frères et sœurs
print("Nombre total de frères et sœurs:", len(siblings))

# Exo 5. Ajouter père et mère (via conversion)
father = "Koffi"
mother = "Ablavi"
family_list = list(siblings)
family_list.extend([father, mother])
Family_Members = tuple(family_list)
print("Membres de la famille:", Family_Members)
