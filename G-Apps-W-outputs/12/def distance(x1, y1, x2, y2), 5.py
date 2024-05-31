
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def solve_megacity(n, s, locations):
    total_population = s
    for location in locations:
        total_population += location[2]

    if total_population >= 1000000:
        return 0.0

    min_radius = float('inf')
    for location in locations:
        dist_to_center = distance(0, 0, location[0], location[1])
        min_radius = min(min_radius, max(0, dist_to_center - location[2]))

    if s >= 1000000:
        return min_radius

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, k1 = locations[i]
            x2, y2, k2 = locations[j]
            dist = distance(x1, y1, x2, y2)
            for ratio in [k1 / (k1 + k2), k2 / (k1 + k2)]:
                total_population = s + k1 * ratio + k2 * (1 - ratio)
                min_radius = min(min_radius, max(0, dist * ratio - total_population))

    if total_population < 1000000:
        return -1
    return min_radius

# Input
n, s = map(int, input().split())
locations = []
for _ in range(n):
    x, y, k = map(int, input().split())
    locations.append((x, y, k))

# Output
result = solve_megacity(n, s, locations)
print("{:.7f}".format(result))
