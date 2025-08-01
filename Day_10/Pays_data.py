from Pays_data import countries_data  # Liste de dictionnaires, chaque pays avec ses infos

# I. Nombre total de langues uniques
def nombre_total_langues():
    toutes_langues = set()
    for pays in countries_data:
        toutes_langues.update(pays.get("languages", []))
    print(" Nombre total de langues :", len(toutes_langues))

# II. 10 langues les plus parlées
def dix_langues_plus_parlees():
    compteur_langues = {}
    for pays in countries_data:
        for langue in pays.get("languages", []):
            compteur_langues[langue] = compteur_langues.get(langue, 0) + 1

    top_10 = sorted(compteur_langues.items(), key=lambda x: x[1], reverse=True)[:10]
    print(" 10 langues les plus parlées :")
    for langue, count in top_10:
        print(f" - {langue}: {count} pays")

# III. 10 pays les plus peuplés
def dix_pays_plus_peuples():
    top_10 = sorted(countries_data, key=lambda x: x.get("population", 0), reverse=True)[:10]
    print(" 10 pays les plus peuplés :")
    for pays in top_10:
        print(f" - {pays['name']}: {pays['population']:,}")
