
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def can_become_megacity(n, s, locations):
    total_population = s
    min_radius = float('inf')
    
    for x, y, k in locations:
        d = distance(0, 0, x, y)
        min_radius = min(min_radius, d)
        total_population += k

    if total_population < 1000000:
        print(-1)
    else:
        print(max(min_radius, math.sqrt(total_population)))

# Input parsing
n, s = map(int, input().split())
locations = []
for _ in range(n):
    x, y, k = map(int, input().split())
    locations.append((x, y, k))

can_become_megacity(n, s, locations)
