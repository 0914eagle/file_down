
def is_palindrome(a):
    return a == a[::-1]

def is_subsequence(a, b):
    i = 0
    for j in range(len(b)):
        if i < len(a) and a[i] == b[j]:
            i += 1
    return i == len(a)

def is_palindrome_subsequence(a):
    for i in range(len(a)):
        for j in range(i + 3, len(a) + 1):
            if is_palindrome(a[i:j]):
                return True
    return False

def solve(a):
    for i in range(len(a) - 2):
        if is_palindrome_subsequence(a[i:]):
            return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

