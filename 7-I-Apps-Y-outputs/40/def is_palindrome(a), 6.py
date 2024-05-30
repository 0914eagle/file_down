
def is_palindrome(a):
    return a == a[::-1]

def is_subsequence(a, b):
    i = 0
    for x in b:
        if x == a[i]:
            i += 1
            if i == len(a):
                return True
    return False

def is_palindrome_subsequence(a):
    for i in range(len(a)):
        for j in range(i + 3, len(a) + 1):
            if is_palindrome(a[i:j]):
                return True
    return False

def solve(a):
    for i in range(len(a)):
        for j in range(i + 3, len(a) + 1):
            if is_palindrome(a[i:j]):
                return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(a))

