
pays = ['Estonie', 'Finlande', 'Suède', 'Danemark', 'Norvège', 'Islande']
noms = ['Asabeneh', 'lidiya', 'ermias', 'Abraham']
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import reduce

noms_majuscules = list(map(lambda x: x.upper(), noms))
print("Noms en majuscules (map):", noms_majuscules)

nombres_pairs = list(filter(lambda x: x % 2 == 0, nombres))
print("Nombres pairs (filter):", nombres_pairs)

somme = reduce(lambda x, y: x + y, nombres)
print("Somme des nombres (reduce):", somme)

def salutation_de_base():
    return "Salut à tous !"

def decorateur_upper(func):
    def wrapper():
        return func().upper()
    return wrapper

salutation_modifiée = decorateur_upper(salutation_de_base)
print("Décorateur appliqué:", salutation_modifiée())

def transformer_nom(nom):
    return f"{nom.title()} !"

noms_transformés = list(map(transformer_nom, noms))
print("Noms transformés:", noms_transformés)

print("Liste des pays :")
for country in pays:
    print(country)

print("Liste des noms :")
for name in noms:
    print(name)

print("Liste des nombres :")
for number in nombres:
    print(number)
