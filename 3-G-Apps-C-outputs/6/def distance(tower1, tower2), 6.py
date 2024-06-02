
import math

def distance(tower1, tower2):
    return math.sqrt((tower1[0] - tower2[0])**2 + (tower1[1] - tower2[1])**2)

def max_towers_in_connected_region(n, towers):
    max_towers = 0
    for i in range(n):
        connected_towers = set()
        for j in range(n):
            if i == j:
                continue
            if distance(towers[i], towers[j]) <= 2:
                connected_towers.add(j)
        connected_towers.add(i)
        max_towers = max(max_towers, len(connected_towers))
    return max_towers

# Read input
n = int(input())
towers = []
for _ in range(n):
    x, y = map(float, input().split())
    towers.append((x, y))

# Calculate and output the result
result = max_towers_in_connected_region(n, towers)
print(result)
