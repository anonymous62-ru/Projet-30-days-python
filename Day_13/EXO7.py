# slope = (y2 - y1)/(x2 - x1)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# y = mx + b ⇒ intercept = y - mx
intercept = lambda x, y, m: y - m * x
