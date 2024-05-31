
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def solve_megacity(n, s, locations):
    total_population = 0
    min_radius = float('inf')

    for x, y, k in locations:
        d = distance(0, 0, x, y)
        total_population += k

        if d <= min_radius:
            min_radius = d

    if total_population >= s:
        return max(min_radius, math.sqrt(s))
    else:
        return -1

# Input
n, s = map(int, input().split())
locations = [list(map(int, input().split())) for _ in range(n)]

# Output
result = solve_megacity(n, s, locations)
print(result)
