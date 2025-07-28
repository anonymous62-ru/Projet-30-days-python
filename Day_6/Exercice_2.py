# Exo 1. Déballer les membres de la famille
Family_Members = ('Kodjo', 'Yaw', 'Kossi', 'Akou', 'Dede', 'Afi', 'Koffi', 'Ablavi')
bro1, bro2, bro3, sis1, sis2, sis3, father, mother = Family_Members
print("Frères:", bro1, bro2, bro3)
print("Sœurs:", sis1, sis2, sis3)
print("Parents:", father, mother)

# Exo 2. Créer fruits, légumes, animaux
fruits = ('mango', 'orange', 'banana')
vegetables = ('carrot', 'lettuce', 'tomato')
animal_products = ('milk', 'eggs', 'meat')

food_stuff_tp = fruits + vegetables + animal_products
print("Food Stuff (tuple):", food_stuff_tp)

# Exo 3. Convertir tuple en liste
food_stuff_lt = list(food_stuff_tp)
print("Food Stuff (list):", food_stuff_lt)

# Exo 4. Couper l’article du milieu
middle_index = len(food_stuff_lt) // 2
print("Article du milieu:", food_stuff_lt[middle_index])

# Exo 5. Slicer 3 premiers et 3 derniers éléments
print("3 premiers:", food_stuff_lt[:3])
print("3 derniers:", food_stuff_lt[-3:])

# Exo 6. Supprimer le tuple
del food_stuff_tp
# print(food_stuff_tp)  # (déclencherait une erreur car supprimé)

# Exo 7. Vérifier si élément existe dans tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("'Estonie' est nordique?", 'Estonie' in nordic_countries)
print("'Iceland' est nordique?", 'Iceland' in nordic_countries)
