
from math import sqrt

def solve(n, t, g, r):
    if n == 1:
        return sqrt(2 * 1000)
    else:
        return min(solve(n - 1, t, g, r) + sqrt(2 * 1000), solve(n - 1, (t + g[n - 1]) % (g[n - 1] + r[n - 1]), g, r) + sqrt(2 * 1000) + (g[n - 1] + r[n - 1] - t[n - 1]))

n = int(input())
t = [0] * (n - 1)
g = [0] * (n - 1)
r = [0] * (n - 1)
for i in range(n - 1):
    t[i], g[i], r[i] = map(int, input().split())
print(solve(n, t, g, r))

