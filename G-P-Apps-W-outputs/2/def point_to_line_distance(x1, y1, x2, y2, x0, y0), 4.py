
import math

def point_to_line_distance(x1, y1, x2, y2, x0, y0):
    A = x0 - x1
    B = y0 - y1
    C = x2 - x1
    D = y2 - y1
    dot = A * C + B * D
    len_sq = C * C + D * D
    param = -1
    if len_sq != 0:
        param = dot / len_sq
    if param < 0:
        xx = x1
        yy = y1
    elif param > 1:
        xx = x2
        yy = y2
    else:
        xx = x1 + param * C
        yy = y1 + param * D
    return math.sqrt((x0 - xx) ** 2 + (y0 - yy) ** 2)

def polygon_line_intersection_length(vertices, x1, y1, x2, y2):
    n = len(vertices)
    total_length = 0
    for i in range(n):
        x3, y3 = vertices[i]
        x4, y4 = vertices[(i + 1) % n]
        d1 = point_to_line_distance(x3, y3, x4, y4, x1, y1)
        d2 = point_to_line_distance(x3, y3, x4, y4, x2, y2)
        if (d1 < 1e-9) and (d2 < 1e-9):
            total_length += math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        elif d1 < 1e-9:
            total_length += math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        elif d2 < 1e-9:
            total_length += math.sqrt((x2 - x4) ** 2 + (y2 - y4) ** 2)
        elif d1 * d2 < 0:
            total_length += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return total_length

n, m = map(int, input().split())
vertices = [tuple(map(float, input().split())) for _ in range(n)]
for _ in range(m):
    x1, y1, x2, y2 = map(float, input().split())
    intersection_length = polygon_line_intersection_length(vertices, x1, y1, x2, y2)
    print("{:.10f}".format(intersection_length))
```
