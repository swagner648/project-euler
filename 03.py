n, p = 600851475143, 2
primeFactors = []

while n is not 1:
    if n % p == 0:
        # print("n:", n, "p:", p)
        n = n // p
        primeFactors.append(p)
    p += 1

print("Prime factors:", primeFactors, "\nMax prime factor:", max(primeFactors))
