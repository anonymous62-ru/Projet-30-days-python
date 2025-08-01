#  Somme de tous les nombres de 0 à 100
def somme_totale():
    total = 0
    for i in range(101):
        total += i
    print(f" Somme de tous les nombres (0 à 100) : {total}")  # Résultat attendu : 5050

#  Somme des pairs et des impairs séparément
def somme_pairs_impairs():
    somme_pairs = 0
    somme_impairs = 0
    for i in range(101):
        if i % 2 == 0:
            somme_pairs += i
        else:
            somme_impairs += i
    print(f" Somme des nombres pairs : {somme_pairs}")     # Résultat : 2550
    print(f" Somme des nombres impairs : {somme_impairs}")  # Résultat : 2500
