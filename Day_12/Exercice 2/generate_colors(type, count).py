def generate_colors(color_type, count):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(count)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(count)
    else:
        return " Type de couleur invalide. Utilisez 'hexa' ou 'rgb'."

print(generate_colors('Hexa', 3))
print(generate_colors('rgb', 1)) 
