
from sys import stdin

def solve(N, points):
    x_min, x_max = float('inf'), float('-inf')
    y_min, y_max = float('inf'), float('-inf')
    for x, y, d in points:
        if d == 'R':
            x_max = max(x_max, x)
        elif d == 'L':
            x_min = min(x_min, x)
        elif d == 'U':
            y_max = max(y_max, y)
        elif d == 'D':
            y_min = min(y_min, y)
    return (x_max - x_min) * (y_max - y_min)

N = int(stdin.readline())
points = [tuple(map(str, stdin.readline().split())) for _ in range(N)]
print(solve(N, points))

