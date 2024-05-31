
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def min_radius_to_megacity(n, s, locations):
    total_population = s
    for x, y, k in locations:
        total_population += k

    if total_population < 1000000:
        return -1

    min_radius = float('inf')
    for x, y, k in locations:
        dist = distance(0, 0, x, y)
        min_radius = min(min_radius, dist)

    return max(0, min_radius)

# Input reading
n, s = map(int, input().split())
locations = []
for _ in range(n):
    x, y, k = map(int, input().split())
    locations.append((x, y, k))

# Output the result
result = min_radius_to_megacity(n, s, locations)
print("{:.7f}".format(result))
