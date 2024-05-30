
def can_make_palindrome(n, s):
    for i in range(n // 2):
        if abs(ord(s[i]) - ord(s[n - i - 1])) > 2 or abs(ord(s[i]) - ord(s[n - i - 1])) == 1:
            return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    result = can_make_palindrome(n, s)
    print(result)
```
