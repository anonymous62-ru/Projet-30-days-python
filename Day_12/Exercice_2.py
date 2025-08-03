"""
Exercice – Générateur de couleurs aléatoires (Jour 12)
Crée des couleurs HEXA ou RGB dans un tableau, selon le type et la quantité demandés.
Idéal pour usages graphiques, quiz, palettes ou projet pédagogique.

Auteur : Amèvi Maxime – Projet 30DaysOfPython
"""

import random

def generate_colors(color_type, count):
    """
    Génère une liste de couleurs aléatoires de type 'hexa' ou 'rgb'.
    
    Paramètres :
    - color_type (str) : 'hexa' ou 'rgb'
    - count (int) : nombre de couleurs à générer

    Retour :
    - Liste de chaînes représentant les couleurs
    """
    color_type = color_type.lower()
    colors = []

    for _ in range(count):
        if color_type == 'hexa':
            color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        elif color_type == 'rgb':
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = f"RGB({r}, {g}, {b})"
        else:
            return " Type de couleur invalide. Utilisez 'hexa' ou 'rgb'."
        colors.append(color)
    
    return colors

#  Tests rapides
if __name__ == "__main__":
    print(" Génération HEXA :", generate_colors('hexa', 3))
    print(" Génération RGB :", generate_colors('rgb', 2))
