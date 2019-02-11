from math import gcd

def run(n):
    for i in range(20, 0, -1):
        if n % i:
            n = run(n * i // gcd(n, i))
            return n
    return n

print("Smallest number evenly divisble:", run(1))