#  Itérer de 0 à 10 avec une boucle for et while
def boucle_croissante():
    print(" Boucle for de 0 à 10 :")
    for i in range(11):
        print(i, end=' ')
    print("\n Boucle while de 0 à 10 :")
    i = 0
    while i <= 10:
        print(i, end=' ')
        i += 1
    print()

#  Itérer de 10 à 0 avec une boucle for et while
def boucle_decroissante():
    print(" Boucle for de 10 à 0 :")
    for i in range(10, -1, -1):
        print(i, end=' ')
    print("\n Boucle while de 10 à 0 :")
    i = 10
    while i >= 0:
        print(i, end=' ')
        i -= 1
    print()

#  Triangle avec print() et #
def triangle_hashtags():
    print(" Triangle progressif :")
    for i in range(1, 8):
        print("#" * i)

#  Boucles imbriquées : motif en grille
def grille_hashtags():
    print(" Motif grille :")
    for _ in range(6):  # lignes
        print("# " * 13)

#  Table de multiplication : i x i
def table_identite():
    print(" Multiplications i x i :")
    for i in range(11):
        print(f"{i} x {i} = {i*i}")

# Itération sur liste de technos
def lister_technos():
    technos = ['python', 'numpy', 'pandas', 'django', 'flask']
    print(" Technologies Python :")
    for techno in technos:
        print(techno)

#  Nombres pairs de 0 à 100
def imprimer_pairs():
    print(" Nombres pairs :")
    for i in range(101):
        if i % 2 == 0:
            print(i, end=' ')
    print()

# Nombres impairs de 0 à 100
def imprimer_impairs():
    print(" Nombres impairs :")
    for i in range(101):
        if i % 2 != 0:
            print(i, end=' ')
    print()
