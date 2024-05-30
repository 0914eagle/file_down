
def can_be_palindrome(n, s):
    for i in range(n // 2):
        if abs(ord(s[i]) - ord(s[n-1-i])) > 2 or abs(ord(s[i]) - ord(s[n-1-i])) == 1:
            return "NO"
    return "YES"

# Input
T = int(input())
for _ in range(T):
    n = int(input())
    s = input()

    # Check if string can be transformed into palindrome
    result = can_be_palindrome(n, s)
    print(result)
