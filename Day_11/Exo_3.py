import keyword

#  Vérifier si un nombre est premier
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

#  Vérifier si tous les éléments d'une liste sont uniques
def all_unique(lst):
    return len(set(lst)) == len(lst)

#  Vérifier si tous les éléments d'une liste sont du même type
def same_type(lst):
    return all(isinstance(x, type(lst[0])) for x in lst)

#  Vérifier si une variable est un nom valide en Python
def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)

pays = [
    {"name": "Chine", "population": 1444216107, "languages": ["Chinois"]},
    {"name": "Inde", "population": 1393409038, "languages": ["Hindi", "Anglais"]},
    {"name": "USA", "population": 331893745, "languages": ["Anglais"]},
    # ...
]
#  Extraire les langues les plus parlées
def most_spoken_languages(pays_data, top_n=10):
    lang_counter = {}
    for country in pays_data:
        for lang in country.get("languages", []):
            lang_counter[lang] = lang_counter.get(lang, 0) + 1
    sorted_langs = sorted(lang_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_langs[:top_n]

#  Extraire les pays les plus peuplés
def most_populated_countries(pays_data, top_n=10):
    sorted_countries = sorted(pays_data, key=lambda x: x["population"], reverse=True)
    return sorted_countries[:top_n]
