from Pays import countries  # La liste `countries` est importée depuis le fichier

def pays_avec_land():
    resultats = []
    for pays in countries:
        if "land" in pays:
            resultats.append(pays)
    print(" Pays contenant 'land' :", resultats)
