
def checkPalindrome(n, maxPal):
    if str(n) == str(n)[::-1]:
        # print("PALINDROME:", maxPal)
        return max(n, maxPal)
    return maxPal

maxPalindrome = 0
for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        maxPalindrome = checkPalindrome(a * b, maxPalindrome)

print("Largest palindrome:", maxPalindrome)