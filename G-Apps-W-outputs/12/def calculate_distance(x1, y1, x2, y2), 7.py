
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_megacity_possible(n, s, locations):
    total_population = s
    for location in locations:
        total_population += location[2]
    
    if total_population < 1000000:
        return -1
    
    distances = []
    for location in locations:
        distances.append(calculate_distance(0, 0, location[0], location[1]) - math.sqrt(location[2]))
    
    distances.sort()
    
    current_population = s
    for i, dist in enumerate(distances):
        current_population += locations[i][2]
        if current_population >= 1000000:
            return max(dist, 0)
    
    return -1

# Input reading
n, s = map(int, input().split())
locations = []
for _ in range(n):
    x, y, k = map(int, input().split())
    locations.append((x, y, k))

# Calculate and print the minimum radius
result = is_megacity_possible(n, s, locations)
print(result)
