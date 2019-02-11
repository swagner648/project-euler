primes = [2]
n = 3

while len(primes) < 10001:
    prime = True
    for p in primes:
        if not n % p:
            prime = False
            break
    if prime:
        primes.append(n)
        print(len(primes), primes)
    n += 2

print("10001st prime:", primes[10000])