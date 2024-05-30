
def is_palindrome(a):
    n = len(a)
    for i in range(n):
        if a[i] != a[n - i - 1]:
            return False
    return True

def is_subpalindrome(a):
    n = len(a)
    for i in range(n):
        for j in range(i + 2, n + 1):
            if j - i < 3:
                continue
            if is_palindrome(a[i:j]):
                return True
    return False

def solve(a):
    n = len(a)
    if n < 3:
        return "NO"
    if is_subpalindrome(a):
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

