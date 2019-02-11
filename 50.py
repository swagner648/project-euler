from eulerlib.prime_numbers import *

primes = primes(1000000)
maxCount = 1
ans = 0

for i in range(1, len(primes)):
    count = 1
    sum = primes[i]
    for j in range(i + 1, len(primes)):
        count += 1
        sum += primes[j]
        if sum > 1000000:
            break
        if is_prime(sum) and count > maxCount:
            maxCount = count
            ans = sum
print(ans)