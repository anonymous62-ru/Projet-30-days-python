a = 10
b = 3
print("Addition:", a + b)
print("Soustraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)         # Donne un float
print("Division entière:", a // b) # Sans reste
print("Modulo (reste):", a % b)
print("Exponentiation:", a ** b)   # a^b

x = 5
x += 2    # équivaut à x = x + 2
x *= 3    # équivaut à x = x * 3
x /= 2    # équivaut à x = x / 2
print("Valeur de x après affectations:", x)

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("True and False :", True and False)
print("True or False  :", True or False)
print("not True       :", not True)

word = "python"
print("'py' in word :", 'py' in word)
print("'on' not in word :", 'on' not in word)

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b    :", a is b)      # True, même objet
print("a is c    :", a is c)      # False, objets identiques mais séparés
print("a == c    :", a == c)      # True, contenus identiques
