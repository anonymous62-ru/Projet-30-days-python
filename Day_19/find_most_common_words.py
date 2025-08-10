from collections import Counter
import re

def find_most_common_words(filepath_or_text, top_n):
    """
    Trouve les mots les plus fréquents dans un texte ou fichier.

    Args:
        filepath_or_text (str): Chemin vers le fichier ou texte brut
        top_n (int): Nombre de mots les plus fréquents à retourner

    Returns:
        list: Liste de tuples (fréquence, mot)
    """
    try:
        if filepath_or_text.endswith('.txt'):
            with open(filepath_or_text, 'r', encoding='utf-8') as f:
                text = f.read()
        else:
            text = filepath_or_text

        words = re.findall(r'\b\w+\b', text.lower())
        counter = Counter(words)
        return counter.most_common(top_n)
    except FileNotFoundError:
        return f"Fichier introuvable : {filepath_or_text}"
