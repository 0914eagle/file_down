
def can_be_palindrome(n, s):
    for i in range(n//2):
        if abs(ord(s[i]) - ord(s[n-1-i])) > 2 or abs(ord(s[i]) - ord(s[n-1-i])) == 1:
            return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    print(can_be_palindrome(n, s))
