
def can_be_palindrome(n, s):
    for i in range(n//2):
        diff = abs(ord(s[i]) - ord(s[n-i-1]))
        if diff != 0 and diff != 2:
            return "NO"
    return "YES"

# Input
T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    
    # Check if string can be transformed into a palindrome
    result = can_be_palindrome(n, s)
    print(result)
```
