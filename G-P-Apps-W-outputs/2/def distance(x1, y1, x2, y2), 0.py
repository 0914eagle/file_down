
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def point_to_line_distance(x1, y1, x2, y2, x0, y0):
    A = x0 - x1
    B = y0 - y1
    C = x2 - x1
    D = y2 - y1

    dot = A * C + B * D
    len_sq = C * C + D * D
    param = -1
    if len_sq != 0:  # in case of 0 length line
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

    return distance(x0, y0, xx, yy)

def polygon_to_line_distance(polygon, x1, y1, x2, y2):
    total_distance = 0
    for i in range(len(polygon) - 1):
        x0 = polygon[i][0]
        y0 = polygon[i][1]
        x3 = polygon[i + 1][0]
        y3 = polygon[i + 1][1]
        total_distance += point_to_line_distance(x0, y0, x3, y3, x1, y1)
    total_distance += point_to_line_distance(polygon[-1][0], polygon[-1][1], polygon[0][0], polygon[0][1], x1, y1)
    return total_distance

n, m = map(int, input().split())

polygon = []
for _ in range(n):
    x, y = map(float, input().split())
    polygon.append((x, y))

for _ in range(m):
    x1, y1, x2, y2 = map(float, input().split())
    result = polygon_to_line_distance(polygon, x1, y1, x2, y2)
    print("{:.10f}".format(result))

```
