from functools import reduce

pays = ['Estonie', 'Finlande', 'Suède', 'Danemark', 'Norvège', 'Islande']
noms = ['Asabeneh', 'lidiya', 'ermias', 'Abraham']
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pays_majuscules = list(map(str.upper, pays))

nombres_positions = list(map(lambda x: nombres.index(x), nombres))

noms_majuscules = list(map(str.upper, noms))

pays_land = list(filter(lambda x: 'land' in x.lower(), pays))

pays_6_caracteres = list(filter(lambda x: len(x) == 6, pays))

pays_6_plus = list(filter(lambda x: len(x) >= 6, pays))

pays_E = list(filter(lambda x: x.startswith('E'), pays))

pays_chaînés = list(map(lambda x: x + " !", map(str.upper, pays)))

somme_nombres = reduce(lambda x, y: x + y, nombres)

phrase = reduce(lambda x, y: x + ", " + y, pays[:-1]) + " et " + pays[-1] + " sont en Europe du Nord"

def categorize_countries(patterns):
    return list(filter(lambda x: any(p in x.lower() for p in patterns), pays))

motifs = ['terre', 'ia', 'île', 'stan']
résultat_categorisé = categorize_countries(motifs)

def countries_by_initial():
    dico = {}
    for country in pays:
        lettre = country[0].upper()
        dico[lettre] = dico.get(lettre, 0) + 1
    return dico

def get_first_ten_countries(pays_liste):
    return pays_liste[:10]

def get_last_ten_countries(pays_liste):
    return pays_liste[-10:]
