
import sys
input = sys.stdin.readline

def inverse(x):
    return pow(x, 998244351, 998244353)

def solve(n, m, d, a, b):
    d.sort(reverse=True)
    a.sort(reverse=True)
    b.sort(reverse=True)
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % 998244353
    inv_fact = [inverse(fact[i]) for i in range(n + 1)]
    def prob(i, j):
        return inv_fact[i] * inv_fact[n - i] * fact[n] % 998244353
    def calc(a, b):
        res = 0
        for i in range(n):
            if a[0] == 0:
                res += d[i] * prob(i, n)
            elif a[0] > 0 and d[i] >= b[0]:
                res += prob(i, n)
            elif a[0] > 0 and d[i] < b[0]:
                pass
            a.pop(0)
            b.pop(0)
        return res % 998244353
    return [calc(a[:], b[:]) for _ in range(m)]

n, m = map(int, input().split())
d = list(map(int, input().split()))
a = []
b = []
for _ in range(m):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
res = solve(n, m, d, a, b)
for x in res:
    print(x)

