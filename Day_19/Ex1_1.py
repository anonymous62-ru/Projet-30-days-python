def count_lines_and_words(filepath):
    """
    Compte le nombre de lignes et de mots dans un fichier texte.

    Args:
        filepath (str): Chemin vers le fichier .txt

    Returns:
        tuple: (nombre_de_lignes, nombre_de_mots)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
        return line_count, word_count
    except FileNotFoundError:
        return f"Fichier introuvable : {filepath}"
