import random

def shuffle_list(lst):
    """
    Mélange une liste donnée sans modifier l'originale.
    Exemple : [1, 2, 3] ➜ [3, 1, 2]
    """
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled
