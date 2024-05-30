
import math

def point_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def line_intersection_distance(x1, y1, x2, y2, x3, y3, x4, y4):
    px = x2 - x1
    py = y2 - y1
    qx = x4 - x3
    qy = y4 - y3
    
    det = px * qy - py * qx
    if det == 0:
        return 0
    
    t = ((x1 - x3) * qy - (y1 - y3) * qx) / det
    u = ((x1 - x2) * py - (y1 - y2) * px) / det
    
    if t >= 0 and t <= 1 and u >= 0 and u <= 1:
        intersection_x = x1 + t * px
        intersection_y = y1 + t * py
        return point_distance(intersection_x, intersection_y, x1, y1)
    
    return 0

def polygon_line_intersection(n, polygon, line):
    total_distance = 0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        distance = line_intersection_distance(x1, y1, x2, y2, line[0], line[1], line[2], line[3])
        total_distance += distance
    return total_distance

n, m = map(int, input().split())
polygon = [tuple(map(float, input().split())) for _ in range(n)]

for _ in range(m):
    line = tuple(map(float, input().split()))
    result = polygon_line_intersection(n, polygon, line)
    print("{:.20f}".format(result))
```
