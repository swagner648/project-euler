from eulerlib.prime_numbers import *
import itertools


for p in primes(10000100):
    if p > 9999999:
        for i in range(1, 8):
            for j in itertools.permutations(([1] * i) + ([0] * (8 - i))):
                for k in range(0, 10):

