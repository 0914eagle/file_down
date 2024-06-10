
from math import sqrt
def solve(n, times):
    dist = 0
    for i in range(n-1):
        dist += sqrt(g[i]**2 + r[i]**2)
    return dist

n = int(input())
times = []
for _ in range(n-1):
    t, g, r = map(int, input().split())
    times.append((t, g, r))
print(solve(n, times))

