# Définition initiale
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Exo 1 Trouver la longueur de l'ensemble
print("Nombre d'entreprises :", len(it_companies))  # Résultat : 7

# Exo 2 Ajouter "Twitter"
it_companies.add("Twitter")
print("Après ajout de Twitter :", it_companies)

# Exo 3 Ajouter plusieurs entreprises à la fois
it_companies.update(['Airbnb', 'Spotify', 'Uber'])
print("Après ajout multiple :", it_companies)

# Exo 4 Supprimer une entreprise
it_companies.remove("Oracle")  # Supprime "Oracle"
print("Après suppression d'Oracle :", it_companies)

# Exo 5 Différence entre remove() et discard()
# remove() ➤ génère une erreur si l’élément n’existe pas
# discard() ➤ ne génère PAS d’erreur, même si l’élément est absent

it_companies.discard("Netflix")  # Aucun problème si Netflix n'existe pas
print("Après discard de Netflix (non présent) :", it_companies)

# it_companies.remove("Netflix")  # 💥 Erreur si Netflix n’est pas dans le set
