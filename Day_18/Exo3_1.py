import re
from collections import Counter

phrase = """'% i $ am @% a% tea @ cher%, & & i lo% # ve% tea @ ching%;. Il n'y a rien
; & as & mo @ re-récompense comme educa @ ting & & & @ emp% o @ wering peo
@ ple. ; J'ai trouvé le thé @ ching m% o @ re intéressant tha @ n tout autre% jo @ bs.
% Do @ es thi% s mo @ tivate yo @ u pour être un thé @ cher !?'"""

# Étape 1 : suppression des caractères spéciaux
texte_nettoye = re.sub(r"[^\w\s]", "", phrase)

# Étape 2 : suppression des espaces superflus
texte_nettoye = re.sub(r"\s+", " ", texte_nettoye).strip()

# Étape 3 : mise en minuscule
texte_nettoye = texte_nettoye.lower()

print("Texte nettoyé :", texte_nettoye)

# Découpage en mots
mots = texte_nettoye.split()

# Comptage des fréquences
frequences = Counter(mots)

# Top 3
top_3 = frequences.most_common(3)
print("Top 3 mots :", top_3)
