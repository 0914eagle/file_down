
from math import sqrt

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def find_bulkhead_placements(C, vertices):
    N = len(vertices)
    bulkhead_placements = []
    for i in range(N):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % N]
        x3, y3 = vertices[(i + 2) % N]
        a = area(x1, y1, x2, y2, x3, y3)
        if a >= C:
            bulkhead_placements.append((x2 + x3) / 2.0)
    return bulkhead_placements

C = int(input())
N = int(input())
vertices = []
for _ in range(N):
    x, y = map(int, input().split())
    vertices.append((x, y))

bulkhead_placements = find_bulkhead_placements(C, vertices)
print(len(bulkhead_placements))
for x in sorted(bulkhead_placements):
    print(x)

