
squareOfSum = sumOfSquares = 0

for i in range(1, 101):
    sumOfSquares += i * i
    squareOfSum += i
squareOfSum *= squareOfSum

print("squareOfSum - sumOfSquares =", squareOfSum - sumOfSquares)