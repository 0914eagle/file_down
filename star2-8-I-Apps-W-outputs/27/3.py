
from itertools import product


def calc(n, r):
    res = 1
    for x in r:
        res *= (n - x + 1)
        res %= 1000000007
    return res


h, w = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
if any(r[i] > c[j] for i, j in product(range(h), range(w))):
    print(0)
else:
    print(calc(h, r) * calc(w, c) % 1000000007)

