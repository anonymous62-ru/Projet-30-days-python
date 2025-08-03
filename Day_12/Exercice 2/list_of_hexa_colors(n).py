import random

def list_of_hexa_colors(n):
    colors = []
    for _ in range(n):
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(hex_color)
    return colors

print(list_of_hexa_colors(3))  