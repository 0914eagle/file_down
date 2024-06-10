
from math import sqrt

def intersect(x1, y1, r1, x2, y2, r2):
    d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if d >= r1 + r2:
        return False
    if d <= abs(r1 - r2):
        return False
    return True

def solve(n, x, y, r):
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if intersect(x[i], y[i], r[i], x[j], y[j], r[j]):
                res = max(res, 2)
    return res

n = int(input())
x = [0] * n
y = [0] * n
r = [0] * n
for i in range(n):
    x[i], y[i], r[i] = map(float, input().split())
print(solve(n, x, y, r))

