from eulerlib import primes

for p in reversed(primes(7654321)):
    digits = sorted(map(int, list(str(p))))
    if digits == list(range(1, digits[len(digits) - 1] + 1)):
        print(p)
        break
