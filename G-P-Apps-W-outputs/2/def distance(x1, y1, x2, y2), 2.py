
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def common_part_length(n, m, polygon_vertices, lines):
    def is_point_inside(x, y, vertices):
        n = len(vertices)
        c = False
        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]
            if ((y1 <= y and y < y2) or (y2 <= y and y < y1)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
                c = not c
        return c

    def line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            return 1 if val > 0 else 2

        o1 = orientation((x1, y1), (x2, y2), (x3, y3))
        o2 = orientation((x1, y1), (x2, y2), (x4, y4))
        o3 = orientation((x3, y3), (x4, y4), (x1, y1))
        o4 = orientation((x3, y3), (x4, y4), (x2, y2))

        if o1 != o2 and o3 != o4:
            return True
        if o1 == 0 and is_point_inside(x1, y1, [(x3, y3), (x4, y4)]):
            return True
        if o2 == 0 and is_point_inside(x2, y2, [(x3, y3), (x4, y4)]):
            return True
        if o3 == 0 and is_point_inside(x3, y3, [(x1, y1), (x2, y2)]):
            return True
        if o4 == 0 and is_point_inside(x4, y4, [(x1, y1), (x2, y2)]):
            return True
        return False

    result = []
    for line in lines:
        x1, y1, x2, y2 = line
        length = 0
        for i in range(n):
            x3, y3 = polygon_vertices[i]
            x4, y4 = polygon_vertices[(i + 1) % n]
            if line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
                length += min(distance(x1, y1, x2, y2), distance(x3, y3, x4, y4))
        result.append(length)

    return result

# Input parsing
n, m = map(int, input().split())
polygon_vertices = [tuple(map(float, input().split())) for _ in range(n)]
lines = [tuple(map(float, input().split())) for _ in range(m)]

# Call the function and print the results
results = common_part_length(n, m, polygon_vertices, lines)
for result in results:
    print("{:.20f}".format(result))

```
