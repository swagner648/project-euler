def findNextPrime(p):
    p += 1
    while p < 2000000 and nums[p] is not 1:
        p += 1
    if p >= 2000000:
        return -1
    return p

nums = [1] * 2000001
primesSum, p = 0, 2

while p > 0:
    primesSum += p
    i = p + p
    while i < 2000000:
        nums[i] = 0
        i += p
    p = findNextPrime(p)

print("Sum of primes < 2,000,000:", primesSum)
