# Exo 1 Convertir les âges en set et comparer
ages = [22, 19, 24, 25, 26, 24, 25, 24]

ages_set = set(ages)
print("Liste complète :", ages)
print("Ensemble unique :", ages_set)

print("Longueur liste :", len(ages))        # Résultat : 8
print("Longueur ensemble :", len(ages_set)) # Résultat : 5

# 💡 La liste est plus longue car elle contient des doublons.
# Le set ne conserve que les âges uniques — utile pour analyser des données sans répétition.

# Exo 2 Différences entre les types de données
data_types = {
    "string": "chaîne de caractères, séquence immuable d'éléments",
    "list": "collection ordonnée, modifiable et indexée",
    "tuple": "collection ordonnée, immuable",
    "set": "collection non ordonnée, non indexée, sans doublons"
}

print("\n📘 Comparaison des types de données :")
for dtype, definition in data_types.items():
    print(f"- {dtype}: {definition}")

# 💡 Chaque type a ses usages : les strings pour du texte, les listes pour des collections dynamiques,
# les tuples pour des données fixes, et les sets pour du tri/filtrage sans doublons.

# Exo 3 Compter les mots uniques d’une phrase
phrase = "I am a teacher and I love to inspire and teach people"
words = phrase.split()
unique_words = set(words)

print("\nPhrase :", phrase)
print("Mots uniques :", unique_words)
print("Nombre de mots uniques :", len(unique_words))  # Résultat : 10

# 💡 Application réelle : retirer les doublons dans un corpus de mots, analyser la richesse lexicale...
