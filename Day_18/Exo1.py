import re
from collections import Counter

paragraphe = """J'adore enseigner. Si vous n'aimez pas enseigner ce que vous pouvez aimer d'autre.
J'adore Python si vous n'aimez pas quelque chose qui peut vous donner toutes les capacités
de développer une application que pouvez-vous aimer d'autre."""

# Nettoyage : suppression des apostrophes, ponctuation, mise en minuscule
texte_nettoye = re.sub(r"[^\w\s]", "", paragraphe.lower())

# Découpage en mots
mots = texte_nettoye.split()

# Comptage des fréquences
frequences = Counter(mots)

# Mot le plus fréquent
mot_plus_frequent = frequences.most_common(1)[0]
print("Mot le plus fréquent :", mot_plus_frequent)
