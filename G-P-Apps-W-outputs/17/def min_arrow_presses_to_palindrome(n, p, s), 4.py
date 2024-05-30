
def min_arrow_presses_to_palindrome(n, p, s):
    p -= 1
    left = p
    right = n - p - 1
    press = 0
    
    if left > right:
        p = n - p - 1
        left, right = right, left
    
    for i in range(n // 2):
        press += min(abs(ord(s[i]) - ord(s[n - i - 1])), 26 - abs(ord(s[i]) - ord(s[n - i - 1]))

    press += min(abs(p), abs(left))
    press += min(abs(p - left), abs(right - p))

    return press

# Input
n, p = map(int, input().split())
s = input()

# Output
print(min_arrow_presses_to_palindrome(n, p, s))
```
