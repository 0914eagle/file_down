
from math import cos

def solve(t, c, m):
    for y in range(h):
        for x in range(w):
            c[(x, y)] = a[x][y] + m * 5 * (cos(t * 3.1415926 / 12) + 1)


a = []
w, h, x, y = map(int, input().split())
m = int(input())
a = [list(map(int, input().split())) for _ in range(h)]

t = 0.0
r = 0.0
c = {}
solve(t, c, m)

t = 12.0
solve(t, c, m)

while t - 1e-9 > 1e-9:
    t = (t + r) / 2
    solve(t, c, m)
    if c[(x, y)] > 0:
        t = r
        r = t
    else:
        r = t

print("{:.0f}".format(t * 60 * m))
