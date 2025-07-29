# Définition des ensembles
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Exo 1 Rejoignez A et B (union)
print("Union de A et B :", A.union(B))
# Tous les éléments uniques combinés

# Exo 2 Trouvez l'intersection entre A et B
print("Intersection de A et B :", A.intersection(B))
# Les éléments communs aux deux ensembles

# Exo 3 A est-il un sous-ensemble de B ?
print("A est sous-ensemble de B :", A.issubset(B))
# Renvoie True si tous les éléments de A sont dans B

# Exo 4 A et B sont-ils disjoints ?
print("A et B sont disjoints :", A.isdisjoint(B))
# True si aucune valeur en commun (ici ce sera False)

# Exo 5 Fusionner A dans B et B dans A
A.update(B)
print("A après fusion avec B :", A)

B.update(A)
print("B après fusion avec A :", B)
# Attention : après cela, A et B seront identiques

# Exo 6 Différence symétrique (ce qui n’est pas commun)
sym_diff = A.symmetric_difference(B)
print("Différence symétrique entre A et B :", sym_diff)
# Normalement vide ici car les deux sont identiques après update()

# Exo 7 Supprimer complètement les ensembles
del A
del B
# A et B n’existent plus dans l’environnement
