import re

texte = """La position de certaines particules sur l'axe X horizontal est -12, -4, -3 et -1 dans le sens
négatif, 0 à l'origine, 4 et 8 dans le sens positif."""

# Extraction des nombres (positifs et négatifs)
nombres = re.findall(r"-?\d+", texte)
points = list(map(int, nombres))

# Distance maximale
distance = max(points) - min(points)
print("Points extraits :", points)
print("Distance maximale :", distance)
