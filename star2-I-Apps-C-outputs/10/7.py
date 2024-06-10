
from math import sqrt

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def solve(C, N, points):
    points = sorted(points, key=lambda p: p[0])
    best_x = []
    best_m = 1
    best_area = area(*points[0], *points[1], *points[2])
    for i in range(1, N - 1):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        x3, y3 = points[i + 1]
        current_area = area(x1, y1, x2, y2, x3, y3)
        if current_area >= best_area:
            best_m += 1
            best_x.append(x2)
            best_area = current_area
    return best_m, best_x

C = int(input())
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

best_m, best_x = solve(C, N, points)
print(best_m)
for x in best_x:
    print(x)

