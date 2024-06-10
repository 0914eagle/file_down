
from math import factorial

def nCk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def inverse(a, m):
    a %= m
    for x in range(1, m):
        if a * x % m == 1:
            return x
    return 1

def solve(n, m, d, a, b):
    res = [0] * m
    for i in range(m):
        if a[i] >= n:
            res[i] = 0
        else:
            res[i] = sum(d[j] for j in range(n) if j < a[i] or d[j] >= b[i])
            for j in range(n):
                if j < a[i] or d[j] >= b[i]:
                    res[i] -= d[j] * nCk(n - 1, j) * inverse(factorial(n - j - 1), 998244353)
                    res[i] %= 998244353
    return res

