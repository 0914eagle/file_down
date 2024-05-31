
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def can_become_megacity(n, s, locations):
    total_population = s
    for location in locations:
        total_population += location[2]

    if total_population >= 1000000:
        return 0.0

    min_radius = float('inf')
    for location in locations:
        distance_to_origin = calculate_distance(0, 0, location[0], location[1])
        min_radius = min(min_radius, distance_to_origin - location[2])

    if s >= 1000000:
        return min_radius
    return max(-1, 1000000 - s)

n, s = map(int, input().split())
locations = [list(map(int, input().split())) for _ in range(n)]

result = can_become_megacity(n, s, locations)
print("{:.7f}".format(result))
