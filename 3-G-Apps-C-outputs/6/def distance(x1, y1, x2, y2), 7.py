
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def find_max_towers(n, towers):
    max_towers = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = towers[i]
            x2, y2 = towers[j]
            dist = distance(x1, y1, x2, y2)
            if dist <= 2:
                max_towers = max(max_towers, 2)
            else:
                max_towers = max(max_towers, 3)
    
    return max_towers

# Read input
n = int(input())
towers = []
for _ in range(n):
    x, y = map(float, input().split())
    towers.append((x, y))

# Add a new tower at the center of existing towers
center_x = sum(x for x, _ in towers) / n
center_y = sum(y for _, y in towers) / n
towers.append((center_x, center_y))

# Find the maximum number of towers in a single connected subregion
result = find_max_towers(n+1, towers)
print(result)
