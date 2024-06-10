
from itertools import accumulate

def solve(n, a, b, h):
    h = list(accumulate([0] + sorted(h)))
    return sum(h[i] // (a - b) for i in range(n + 1))

n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
print(solve(n, a, b, h))

