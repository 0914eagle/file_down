
from itertools import combinations
n = int(input())

A = [int(input()) for i in range(2**n)]
A.sort()

def check(l):
    global A, n
    for i in range(1, 2**n):
        s = A[i]
        for j in range(i):
            if s - A[j] in l:
                break
        else:
            return False
    return True

def solve(i, s):
    global A, n
    if i == n:
        return s

    if check(s):
        return s

    if solve(i+1, s + [0]) is not None:
        return s + [0]
    elif solve(i+1, s + [A[0]]) is not None:
        return s + [A[0]]
    else:
        return None

l = solve(0, [])

if l is not None:
    for i in l:
        print(i)
else:
    print("impossible")
