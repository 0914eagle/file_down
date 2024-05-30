
def can_make_palindrome(n, s):
    for i in range(n // 2):
        diff = abs(ord(s[i]) - ord(s[n - 1 - i]))
        if diff != 0 and diff != 2:
            return "NO"
    return "YES"

# Input parsing
T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    result = can_make_palindrome(n, s)
    print(result)
