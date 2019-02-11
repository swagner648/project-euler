from eulerlib.prime_numbers import *

for n in range(1000, 3333):
    if is_prime(n) and n != 1487:
        digits = sorted(map(int, list(str(n))))
        for i in range(1, 3333):
            a = n + i
            b = a + i
            if is_prime(a) and sorted(map(int, list(str(a)))) == digits and \
                is_prime(b) and sorted(map(int, list(str(b)))) == digits:
                print(str(n) + str(a) + str(b))
