from Pays_data import countries_data

def analyse_donnees_pays():
    toutes_langues = set()
    compteur_langues = {}
    pays_plus_peuples = []

    for pays in countries_data:
        # ✅ Collecte de toutes les langues
        toutes_langues.update(pays.get("languages", []))

        # Comptage des langues
        for langue in pays.get("languages", []):
            compteur_langues[langue] = compteur_langues.get(langue, 0) + 1

        # Stockage des pays avec leur population
        pays_plus_peuples.append((pays["name"], pays.get("population", 0)))

    # 🔢 I. Nombre total de langues
    print(f" Nombre total de langues uniques : {len(toutes_langues)}")

    #  II. 10 langues les plus parlées
    top_langues = sorted(compteur_langues.items(), key=lambda x: x[1], reverse=True)[:10]
    print("\n🌍 Dix langues les plus parlées :")
    for langue, count in top_langues:
        print(f" - {langue}: {count} pays")

    # 🏆 III. 10 pays les plus peuplés
    top_pays = sorted(pays_plus_peuples, key=lambda x: x[1], reverse=True)[:10]
    print("\n🏆 Dix pays les plus peuplés :")
    for nom, population in top_pays:
        print(f" - {nom}: {population:,}")

if __name__ == "__main__":
    analyse_donnees_pays()
