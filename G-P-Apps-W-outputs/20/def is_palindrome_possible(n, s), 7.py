
def is_palindrome_possible(n, s):
    for i in range(n//2):
        diff = abs(ord(s[i]) - ord(s[n-1-i]))
        if diff != 0 and diff != 2:
            return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    print(is_palindrome_possible(n, s))
