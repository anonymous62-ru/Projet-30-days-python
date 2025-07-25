# Exercices Python — Jour 3

# Pente et distance entre deux points
x1, y1 = 2, 2
x2, y2 = 6, 10
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
slope = (y2 - y1) / (x2 - x1)

print(" Distance entre (2,2) et (6,10):", distance)
print(" Pente entre (2,2) et (6,10):", slope)

# Résolution pour y = 2x - 2
x = 4
y = 2 * x - 2
print(f" Pour x = {x}, y = 2x - 2 → y = {y}")

# Évaluation de l'expression y = x² + 6x + 9
x_values = [0, 1, -3]
print(" Résultats pour y = x² + 6x + 9 :")
for x in x_values:
    y = x**2 + 6*x + 9
    print(f"👉 x = {x}, y = {y}")

# Vérifier si l'expression est factorisable
# y = x² + 6x + 9 peut être réécrit en (x + 3)²
def is_perfect_square_trinomial(a, b, c):
    return b**2 == 4 * a * c

a, b, c = 1, 6, 9
print(" Trinôme parfait ", is_perfect_square_trinomial(a, b, c))
