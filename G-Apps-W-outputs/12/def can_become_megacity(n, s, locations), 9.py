
import math

def can_become_megacity(n, s, locations):
    total_population = s
    distances = []
    
    for x, y, k in locations:
        distance = math.sqrt(x**2 + y**2)
        distances.append((distance, k))
        total_population += k
    
    if total_population < 1000000:
        return -1
    
    distances.sort()
    
    curr_population = s
    for i in range(n):
        curr_population += distances[i][1]
        if curr_population >= 1000000:
            return distances[i][0]
    
    return -1

# Input parsing
n, s = map(int, input().split())
locations = []
for _ in range(n):
    x, y, k = map(int, input().split())
    locations.append((x, y, k))

# Output
result = can_become_megacity(n, s, locations)
print(result)
