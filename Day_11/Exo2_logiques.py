import math
from collections import Counter

# 1️⃣ Compter pairs et impairs dans une plage
def evens_and_odds(n):
    evens = len([i for i in range(n + 1) if i % 2 == 0])
    odds = len([i for i in range(n + 1) if i % 2 != 0])
    return f"🔢 Nombre de cotes : {odds}\n🧮 Nombre d'evens : {evens}"

# 2️⃣ Factorielle d’un entier
def factorial(n):
    if n < 0:
        return "❌ Entier négatif"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 3️⃣ Vérifier si un paramètre est vide
def is_empty(param):
    return param in ("", None, [], {}, set(), tuple()) or param == 0

# 4️⃣ Statistiques sur une liste numérique
def calculer_mean(lst):
    return sum(lst) / len(lst)

def calculer_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def calculer_mode(lst):
    counts = Counter(lst)
    max_count = max(counts.values())
    mode = [k for k, v in counts.items() if v == max_count]
    return mode if len(mode) < len(lst) else "Pas de mode (distribution uniforme)"

def calculer_range(lst):
    return max(lst) - min(lst)

def calculer_variance(lst):
    mean = calculer_mean(lst)
    return sum((x - mean)**2 for x in lst) / len(lst)

def calculer_std(lst):
    return math.sqrt(calculer_variance(lst))
