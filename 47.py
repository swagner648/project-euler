from eulerlib.numtheory import Divisors

divisors = Divisors(200000)
n = 1
while True:
    if all(len(divisors.prime_factors(x)) == 4 for x in list(range(n, n + 4))):
        print(n)
        break
    n += 1