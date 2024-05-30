
import math

def point_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3
    p1 = dy2 * (x3 - x1) - dx2 * (y3 - y1)
    p2 = dy2 * (x3 - x2) - dx2 * (y3 - y2)
    p3 = dy1 * (x1 - x3) - dx1 * (y1 - y3)
    p4 = dy1 * (x1 - x4) - dx1 * (y1 - y4)
    
    if p1 * p2 < 0 and p3 * p4 < 0:
        return point_distance(x1, y1, x2, y2)
    else:
        return 0

n, m = map(int, input().split())
polygon = []
for _ in range(n):
    x, y = map(float, input().split())
    polygon.append((x, y))

for _ in range(m):
    x1, y1, x2, y2 = map(float, input().split())
    result = 0
    for i in range(n):
        x3, y3 = polygon[i]
        x4, y4 = polygon[(i + 1) % n]
        result += line_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
    print("{:.20f}".format(result))
```

