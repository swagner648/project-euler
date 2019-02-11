import itertools

sum = 0
divisible_conditions = [[1, 2], [2, 3], [3, 5], [4, 7], [5, 11], [6, 13], [7, 17]]
for n in itertools.permutations(range(0, 10)):
    if all(int(''.join(str(s) for s in n[i[0]:i[0] + 3])) % i[1] == 0
           for i in divisible_conditions):
        sum += int(''.join(str(s) for s in n))
print(sum)

