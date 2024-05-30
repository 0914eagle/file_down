
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    def cross_product(x1, y1, x2, y2):
        return x1 * y2 - x2 * y1

    def on_segment(x1, y1, x2, y2, x3, y3):
        return min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2)

    d1 = cross_product(x4 - x3, y4 - y3, x1 - x3, y1 - y3)
    d2 = cross_product(x4 - x3, y4 - y3, x2 - x3, y2 - y3)
    d3 = cross_product(x2 - x1, y2 - y1, x3 - x1, y3 - y1)
    d4 = cross_product(x2 - x1, y2 - y1, x4 - x1, y4 - y1)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return distance(x1, y1, x3, y3)
    elif d1 == 0 and on_segment(x3, y3, x4, y4, x1, y1):
        return distance(x1, y1, x3, y3)
    elif d2 == 0 and on_segment(x3, y3, x4, y4, x2, y2):
        return distance(x2, y2, x3, y3)
    elif d3 == 0 and on_segment(x1, y1, x2, y2, x3, y3):
        return distance(x3, y3, x1, y1)
    elif d4 == 0 and on_segment(x1, y1, x2, y2, x4, y4):
        return distance(x4, y4, x1, y1)
    else:
        return 0

n, m = map(int, input().split())
points = [tuple(map(float, input().split())) for _ in range(n)]
lines = [tuple(map(float, input().split())) for _ in range(m)]

for line in lines:
    length = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        x3, y3, x4, y4 = line
        length += line_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
    print("{:.20f}".format(length))
```
