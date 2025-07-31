# 1️⃣ Vérification de l’âge pour apprendre à conduire
def verifier_age():
    age = int(input("🧍 Entrez votre âge : "))
    if age >= 18:
        print("✅ Vous êtes assez vieux pour apprendre à conduire.")
    else:
        print(f"⏳ Vous avez besoin de {18 - age} ans de plus pour apprendre à conduire.")

# 2️⃣ Comparaison d’âges
def comparer_age():
    my_age = 25  # Ton âge (à adapter si besoin)
    your_age = int(input("👤 Entrez votre âge : "))
    difference = abs(my_age - your_age)

    if your_age > my_age:
        print(f"🧓 Vous avez {difference} {'an' if difference == 1 else 'ans'} de plus que moi.")
    elif your_age < my_age:
        print(f"🧑 J’ai {difference} {'an' if difference == 1 else 'ans'} de plus que vous.")
    else:
        print("👯 Nous avons le même âge !")

# 3️⃣ Comparaison de deux nombres
def comparer_nombres():
    a = int(input("🔢 Entrez le premier nombre : "))
    b = int(input("🔢 Entrez le deuxième nombre : "))
    if a > b:
        print(f"📈 {a} est supérieur à {b}")
    elif a < b:
        print(f"📉 {a} est plus petit que {b}")
    else:
        print(f"⚖️ {a} est égal à {b}")
