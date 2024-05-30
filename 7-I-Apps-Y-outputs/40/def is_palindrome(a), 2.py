
def is_palindrome(a):
    return a == a[::-1]

def is_subsequence(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == len(a)

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
                return 'YES'
    return 'NO'

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

