import string
import numpy as np

triangle_nums = [0.5 * n * (n + 1) for n in range(1, 100)]
data = open('42_data.txt', 'r').read().replace('\"', '').split(',')
alphabet = dict(zip(string.ascii_letters, [ord(c) % 32 for c in string.ascii_letters]))
total = 0
for word in data:
    value = np.sum([alphabet[i] for i in word])
    if value in triangle_nums:
        total += 1
print(total)