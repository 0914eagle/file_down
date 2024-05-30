
def can_make_palindrome(n, s):
    for i in range(n // 2):
        if abs(ord(s[i]) - ord(s[n - i - 1])) not in [0, 2]:
            return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    print(can_make_palindrome(n, s))
```
