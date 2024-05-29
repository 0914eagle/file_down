
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def can_destroy(minion_x, minion_y, village_x, village_y, village_radius, attack_radius):
    distance = calculate_distance(minion_x, minion_y, village_x, village_y)
    return distance >= village_radius + attack_radius

def max_destroyed_minions(villages, minions, attack_radius):
    max_destroyed = 0
    for minion in minions:
        destroyed = 0
        for village in villages:
            if can_destroy(minion[0], minion[1], village[0], village[1], village[2], attack_radius):
                destroyed += 1
        max_destroyed = max(max_destroyed, destroyed)
    return max_destroyed

def solve_tower_defense(n, m, r, villages, minions):
    return max_destroyed_minions(villages, minions, r)

# Input parsing
n, m, r = map(int, input().split())
villages = []
for _ in range(n):
    village = list(map(int, input().split()))
    villages.append(village)

minions = []
for _ in range(m):
    minion = list(map(int, input().split()))
    minions.append(minion)

# Solve the tower defense problem
result = solve_tower_defense(n, m, r, villages, minions)
print(result)
```
