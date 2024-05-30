
import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def segment_intersection_length(x1, y1, x2, y2, x3, y3, x4, y4):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    def on_segment(p, q, r):
        if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
            return True
        return False

    p1 = (x1, y1)
    q1 = (x2, y2)
    p2 = (x3, y3)
    q2 = (x4, y4)

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return dist(p1[0], p1[1], q1[0], q1[1])
    
    if (o1 == 0 and on_segment(p1, p2, q1)) or (o2 == 0 and on_segment(p1, q2, q1)) or \
       (o3 == 0 and on_segment(p2, p1, q2)) or (o4 == 0 and on_segment(p2, q1, q2)):
        return 0

    return 0.0

n, m = map(int, input().split())
polygon = [tuple(map(float, input().split())) for _ in range(n)]

for _ in range(m):
    x1, y1, x2, y2 = map(float, input().split())
    total_length = 0.0
    for i in range(n):
        x3, y3 = polygon[i]
        x4, y4 = polygon[(i+1) % n]
        total_length += segment_intersection_length(x1, y1, x2, y2, x3, y3, x4, y4)
    print("{:.20f}".format(total_length))
```
