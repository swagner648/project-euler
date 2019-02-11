a, b, sumEven = 1, 2, 0

while a <= 4000000:
    if a % 2 == 0:
        print(sumEven, "+", a, "=", sumEven + a)
        sumEven += a
    a, b = b, a + b
    print("a:", a, "b:", b)

print("\nSum of even numbers:", sumEven)