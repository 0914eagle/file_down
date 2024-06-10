
from sys import stdin
from math import sqrt

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def solve(hull, C):
    n = len(hull)
    best = 0
    best_x = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = hull[i]
            x2, y2 = hull[j]
            a = area(x1, y1, x2, y2, 0, 0)
            if a >= C:
                best += 1
                best_x = max(best_x, x2)
    return best, best_x

C = int(stdin.readline())
N = int(stdin.readline())
hull = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
best, best_x = solve(hull, C)
print(best)
print(best_x)

