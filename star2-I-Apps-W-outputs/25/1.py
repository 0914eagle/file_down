
from functools import reduce
from operator import xor

def inverse(x):
    return pow(x, 998244351, 998244353)

def solve(n, m, d, a, b):
    result = [0] * m
    for i in range(n):
        for j in range(m):
            if a[j] > 0 and d[i] < b[j]:
                continue
            if a[j] == 0:
                result[j] += d[i]
            else:
                result[j] += 1
            result[j] %= 998244353
    for i in range(m):
        if result[i] % 998244353 != 0:
            result[i] = result[i] * inverse(998244353 - 1) % 998244353
    return result

n, m = map(int, input().split())
d = list(map(int, input().split()))
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())
result = solve(n, m, d, a, b)
print(*result, sep='\n')

