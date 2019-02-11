def is_hexagonal(x):
    if (0.25 * ((8 * x + 1)**0.5 + 1)).is_integer():
        return True
    return False

def is_pentagonal(x):
    if (1/6 * ((24 * x + 1)**(1/2) + 1)).is_integer():
        return True;
    return False

i = 40755
while True:
    n = i * (i + 1) / 2
    if is_hexagonal(n) and is_pentagonal(n):
        print(n)
        break
    i += 1