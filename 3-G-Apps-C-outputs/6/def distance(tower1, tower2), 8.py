
import math

def distance(tower1, tower2):
    x1, y1 = tower1
    x2, y2 = tower2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def max_towers_in_connected_region(n, towers):
    towers = [(float(x), float(y)) for x, y in towers]
    max_towers = 1
    
    for i in range(n):
        connected_towers = set()
        for j in range(n):
            if i != j and distance(towers[i], towers[j]) <= 2.0:
                connected_towers.add(j)
        
        for j in range(n):
            if i != j:
                for k in range(n):
                    if j != k and i != k and distance(towers[j], towers[k]) <= 2.0:
                        connected_towers.add(k)
        
        max_towers = max(max_towers, len(connected_towers))
    
    return max_towers

# Read input
n = int(input())
towers = [input().split() for _ in range(n)]

# Calculate and print the result
result = max_towers_in_connected_region(n, towers)
print(result)
