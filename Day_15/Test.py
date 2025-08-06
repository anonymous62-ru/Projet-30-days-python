# SyntaxError
print ("bonjour")

# NameError
age =12
print(age)

# IndexError
nombres = [1, 2, 3, 4, 5]
print(nombres[4])
# ModuleNotFoundError
import math
print(math.sqrt(25)) 

# AttributeError
import math
print(math.pi)
# KeyError
user = {'name': 'Amèvi'}
if 'county' in user:
    print(user['county'])
else:
    print("Clé 'county' absente.")


# TypeError
print(4 + int('3'))  # ✅ Affiche 7


# ImportError
resultat = pow(2, 3)  # Renvoie 8


# ValueError
valeur = '12a'
if valeur.isdigit():
    print(int(valeur))
else:
    print(f"'{valeur}' n'est pas un entier valide.")


# ZeroDivisionError
a = 1
b = 0
if b != 0:
    print(a / b)
else:
    print("Impossible de diviser par zéro.")
