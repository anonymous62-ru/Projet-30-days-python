# 3. Création du dictionnaire étudiant
étudiant = {
    "first_name": "Amèvi",
    "last_name": "Kodjo",
    "sexe": "F",
    "âge": 24,
    "marié": False,
    "compétences": ["Python", "Documentation", "Résilience"],
    "pays": "Togo",
    "ville": "Lomé",
    "adresse": {
        "rue": "Rue des Makers",
        "code": "TG0100"
    }
}

# 4. Longueur du dictionnaire étudiant
print(" Longueur :", len(étudiant))

# 8. Obtenir les valeurs comme liste
valeurs = list(étudiant.values())
print(" Valeurs :", valeurs)

# 9. Transformation en liste de tuples
tuples = list(étudiant.items())
print(" Tuples :", tuples)

# 10. Suppression d’un élément (ex : ville)
étudiant.pop("ville")
print(" Ville supprimée :", étudiant)

# 11. Suppression complète du dictionnaire
del étudiant
# print(étudiant)  #  provoquera une erreur si décommenté
