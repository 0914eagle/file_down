
import sys
from math import ceil
input = sys.stdin.readline

def solve(n, a, b, h):
    h = sorted(h, reverse=True)
    res = 0
    while h:
        res += 1
        h[0] -= a
        for i in range(1, n):
            h[i] -= b
        h = [x for x in h if x > 0]
    return res

n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
print(solve(n, a, b, h))

