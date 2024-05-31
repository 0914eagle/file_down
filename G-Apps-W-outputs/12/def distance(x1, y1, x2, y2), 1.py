
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def solve_tomsk(n, s, locations):
    total_population = s
    for location in locations:
        total_population += location[2]
    
    if total_population >= 1000000:
        return 0.0
    
    min_radius = float('inf')
    for location in locations:
        dist_to_location = distance(0, 0, location[0], location[1]) - math.sqrt(location[2])
        min_radius = min(min_radius, dist_to_location)
    
    if total_population == s:
        return -1
    
    return min_radius

# Input
n, s = map(int, input().split())
locations = [list(map(int, input().split())) for _ in range(n)]

# Output
result = solve_tomsk(n, s, locations)
print(result)
