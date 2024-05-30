
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def point_to_line_distance(x, y, x1, y1, x2, y2):
    A = x - x1
    B = y - y1
    C = x2 - x1
    D = y2 - y1
    dot = A * C + B * D
    len_sq = C * C + D * D
    param = -1
    if len_sq != 0:
        param = dot / len_sq
    if param < 0:
        return distance(x, y, x1, y1)
    elif param > 1:
        return distance(x, y, x2, y2)
    else:
        x_intersect = x1 + param * C
        y_intersect = y1 + param * D
        return distance(x, y, x_intersect, y_intersect)

def common_part_length(n, polygon, line):
    result = 0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        result += point_to_line_distance(x1, y1, line[0], line[1], line[2], line[3])
    return result

n, m = map(int, input().split())
polygon = [tuple(map(float, input().split())) for _ in range(n)]
for _ in range(m):
    line = tuple(map(float, input().split()))
    print("{:.20f}".format(common_part_length(n, polygon, line)))
```
