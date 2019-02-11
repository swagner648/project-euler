from eulerlib.prime_numbers import *

n = 3
while True:
    if not is_prime(n):
        if all(not (((n - p) / 2)**0.5).is_integer() for p in primes(n)):
            print(n)
            break
    n += 2

5