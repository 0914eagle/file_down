
from math import sqrt

def point_dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    def cross_product(x1, y1, x2, y2):
        return x1 * y2 - x2 * y1

    def within_bounds(x, y, x1, y1, x2, y2):
        return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

    den = cross_product(x1 - x2, y1 - y2, x3 - x4, y3 - y4)
    if den == 0:
        return 0

    t = cross_product(x3 - x1, y3 - y1, x3 - x4, y3 - y4) / den
    u = -cross_product(x1 - x2, y1 - y2, x3 - x1, y3 - y1) / den

    if 0 <= t <= 1 and 0 <= u <= 1:
        xi = x1 + t * (x2 - x1)
        yi = y1 + t * (y2 - y1)
        xj = x3 + u * (x4 - x3)
        yj = y3 + u * (y4 - y3)
        return point_dist(xi, yi, xj, yj)

    return 0

n, m = map(int, input().split())
polygon = [tuple(map(float, input().split())) for _ in range(n)]
lines = [tuple(map(float, input().split())) for _ in range(m)]

for line in lines:
    line_length = 0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        line_length += line_intersection(x1, y1, x2, y2, line[0], line[1], line[2], line[3])
    print("{:.10f}".format(line_length))
```
