# Toutes les entrées utilisateur sont transformées en float pour précision
<<<<<<< HEAD

=======
>>>>>>> 61670249047c55237751eacae85f79294b759b70
# 1. Zone d'un triangle (area = 0.5 * base * height)
base = float(input("Entrez la base du triangle : "))
height = float(input("Entrez la hauteur du triangle : "))
triangle_area = 0.5 * base * height
<<<<<<< HEAD
print(" Zone du triangle :", triangle_area)
=======
print("Zone du triangle :", triangle_area)
>>>>>>> 61670249047c55237751eacae85f79294b759b70

# 2. Périmètre d'un triangle (perimeter = a + b + c)
a = float(input("Côté A : "))
b = float(input("Côté B : "))
c = float(input("Côté C : "))
triangle_perimeter = a + b + c
<<<<<<< HEAD
print(" Périmètre du triangle :", triangle_perimeter)
=======
print("Périmètre du triangle :", triangle_perimeter)
>>>>>>> 61670249047c55237751eacae85f79294b759b70

# 3. Aire et périmètre d’un rectangle
length = float(input("Longueur du rectangle : "))
width = float(input("Largeur du rectangle : "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
<<<<<<< HEAD
print(" Aire du rectangle :", rectangle_area)
print(" Périmètre du rectangle :", rectangle_perimeter)
=======
print("Aire du rectangle :", rectangle_area)
print("Périmètre du rectangle :", rectangle_perimeter)
>>>>>>> 61670249047c55237751eacae85f79294b759b70

# 4. Aire et circonférence d’un cercle
radius = float(input("Rayon du cercle : "))
pi = 3.14
circle_area = pi * radius ** 2
circle_circumference = 2 * pi * radius
<<<<<<< HEAD
print(" Aire du cercle :", circle_area)
print(" Circonférence du cercle :", circle_circumference)
=======
print("Aire du cercle :", circle_area)
print("Circonférence du cercle :", circle_circumference)
>>>>>>> 61670249047c55237751eacae85f79294b759b70

# 5. Densité = Masse / Volume
mass = float(input("Masse en kg : "))
volume = float(input("Volume en m³ : "))
density = mass / volume
<<<<<<< HEAD
print(" Densité :", density, "kg/m³")
=======
print("Densité :", density, "kg/m³")
>>>>>>> 61670249047c55237751eacae85f79294b759b70

# 6. Distance euclidienne entre deux points
x1, y1 = 2, 2
x2, y2 = 6, 10
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
<<<<<<< HEAD
print(" Distance euclidienne entre (2,2) et (6,10) :", distance)

# 7. Calcul de la pente : m = (y2 - y1) / (x2 - x1)
slope = (y2 - y1) / (x2 - x1)
print(" Pente entre (2,2) et (6,10) :", slope)
=======
print("Distance euclidienne entre (2,2) et (6,10) :", distance)

# 7. Calcul de la pente : m = (y2 - y1) / (x2 - x1)
slope = (y2 - y1) / (x2 - x1)
print("Pente entre (2,2) et (6,10) :", slope)
>>>>>>> 61670249047c55237751eacae85f79294b759b70

# 8. y = 2x - 2
x = float(input("Valeur de x pour y = 2x - 2 : "))
y = 2 * x - 2
<<<<<<< HEAD
print(" y =", y)
=======
print("y =", y)
>>>>>>> 61670249047c55237751eacae85f79294b759b70

# 9. y = x² + 6x + 9
x_values = [0, 1, -3]
for x in x_values:
    y = x**2 + 6*x + 9
    print(f" Pour x={x}, y = {y}")
