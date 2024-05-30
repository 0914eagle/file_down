
import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def segment_length(p1, p2, a, b):
    v1 = [p2[0] - p1[0], p2[1] - p1[1]]
    v2 = [b[0] - a[0], b[1] - a[1]]
    dp1 = v1[0]*a[0] + v1[1]*a[1]
    dp2 = v1[0]*b[0] + v1[1]*b[1]
    if dp1 == dp2:
        return 0
    else:
        return abs(dist(p1, p2) * (dp2 - dp1) / dist(a, b))

def point_in_polygon(polygon, point):
    n = len(polygon)
    count = 0
    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]
        if segment_length(a, b, point, [point[0] + 1e6, point[1]) > 0):
            count += 1
    return count % 2 == 1

def common_length(polygon, line):
    length = 0
    for i in range(len(polygon)):
        a = polygon[i]
        b = polygon[(i + 1) % len(polygon)]
        p1 = [line[0], line[1]]
        p2 = [line[2], line[3]]
        if point_in_polygon([a, b], p1) and point_in_polygon([a, b], p2):
            length += segment_length(p1, p2, a, b)
    return length

n, m = map(int, input().split())
polygon = [tuple(map(float, input().split())) for _ in range(n)]

for _ in range(m):
    line = list(map(float, input().split()))
    print("{:.20f}".format(common_length(polygon, line)))
```
