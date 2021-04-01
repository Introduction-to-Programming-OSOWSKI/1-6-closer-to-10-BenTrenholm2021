def close10(x, y):
    if abs(10 - x) < abs(10 - y):
        return (x)
    elif abs(10 - x) > abs(10 - y):
        return (y)
print(close10(1000, 80))