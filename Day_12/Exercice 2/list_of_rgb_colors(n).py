def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"RGB({r}, {g}, {b})")
    return colors

print(list_of_rgb_colors(3))  