
from math import factorial

def inverse(x):
    return pow(x, 998244351, 998244353)

def solve(n, m, d, a, b):
    res = [0] * m
    for i in range(m):
        if a[i] >= n:
            res[i] = 0
        else:
            x = 0
            for j in range(n):
                if d[j] < b[i]:
                    x += 1
                elif d[j] == b[i]:
                    x += 0.5
            res[i] = int(x * inverse(factorial(n)) % 998244353)
    return res

