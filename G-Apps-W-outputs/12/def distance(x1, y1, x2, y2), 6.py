
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def can_become_megacity(n, s, locations):
    total_population = s
    for x, y, k in locations:
        total_population += k
    
    if total_population >= 1000000:
        return 0.0
    
    min_radius = float('inf')
    for x, y, k in locations:
        d = distance(0, 0, x, y)
        if d - math.sqrt(k) <= min_radius:
            min_radius = d - math.sqrt(k)
    
    if s >= 1000000:
        return 0.0
    elif min_radius == float('inf'):
        return -1
    else:
        return min_radius

# Input parsing
n, s = map(int, input().split())
locations = []
for _ in range(n):
    x, y, k = map(int, input().split())
    locations.append((x, y, k))

result = can_become_megacity(n, s, locations)
print('{:.7f}'.format(result))
