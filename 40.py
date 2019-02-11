string = "".join(str(i) for i in range(1, 800000))
sol = 1
for i in range(7):
    sol *= int(string[10**i - 1])
print(sol)
