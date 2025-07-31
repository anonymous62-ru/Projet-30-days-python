#  Évaluation des notes
def attribuer_note():
    score = int(input(" Entrez le score de l'élève (0-100) : "))
    if 80 <= score <= 100:
        print(" Note : A")
    elif 70 <= score <= 79:
        print(" Note : B")
    elif 60 <= score <= 69:
        print(" Note : C")
    elif 50 <= score <= 59:
        print(" Note : D")
    elif 0 <= score <= 49:
        print(" Note : F")
    else:
        print(" Score invalide. Veuillez entrer un score entre 0 et 100.")

#  Détection de saison selon le mois
def detecter_saison():
    mois = input(" Entrez un mois (en minuscule, ex. 'mars') : ").lower()
    if mois in ['septembre', 'octobre', 'novembre']:
        print(" Saison : automne")
    elif mois in ['décembre', 'janvier', 'février']:
        print(" Saison : hiver")
    elif mois in ['mars', 'avril', 'mai']:
        print(" Saison : printemps")
    elif mois in ['juin', 'juillet', 'août']:
        print(" Saison : été")
    else:
        print(" Mois invalide ou non reconnu.")

#  Vérification et ajout de fruit
def verifier_fruit():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruit = input(" Entrez un fruit : ").lower()
    if fruit in fruits:
        print(" Ce fruit existe déjà dans la liste.")
    else:
        fruits.append(fruit)
        print(" Fruit ajouté ! Liste mise à jour :", fruits)
