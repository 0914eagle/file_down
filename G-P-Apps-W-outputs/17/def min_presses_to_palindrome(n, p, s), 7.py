
def min_presses_to_palindrome(n, p, s):
    p -= 1
    left = p
    right = n - p - 1
    if left > right:
        left, right = right, left
    moves = 0
    for i in range(n // 2):
        diff = abs(ord(s[i]) - ord(s[n - i - 1]))
        moves += min(diff, 26 - diff)
    
    return moves + min(left, right) + abs(left - right)

# Reading input
n, p = map(int, input().split())
s = input().strip()

# Calling the function and printing the result
print(min_presses_to_palindrome(n, p, s))
```
