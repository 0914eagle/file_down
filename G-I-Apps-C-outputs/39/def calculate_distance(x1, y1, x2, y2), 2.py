
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def can_hit_minion(minion_x, minion_y, attack_x, attack_y, attack_radius):
    distance = calculate_distance(minion_x, minion_y, attack_x, attack_y)
    return distance <= attack_radius

def can_hit_village(village_x, village_y, village_radius, attack_x, attack_y, attack_radius):
    distance = calculate_distance(village_x, village_y, attack_x, attack_y)
    return distance + village_radius <= attack_radius

def find_max_destroyed_minions(n, m, r, villages, minions):
    max_destroyed_minions = 0
    for attack_x in range(-20000, 20001):
        for attack_y in range(-20000, 20001):
            valid_attack = True
            destroyed_minions = 0
            for minion_x, minion_y in minions:
                if can_hit_minion(minion_x, minion_y, attack_x, attack_y, r):
                    destroyed_minions += 1
            for village_x, village_y, village_radius in villages:
                if not can_hit_village(village_x, village_y, village_radius, attack_x, attack_y, r):
                    valid_attack = False
                    break
            if valid_attack:
                max_destroyed_minions = max(max_destroyed_minions, destroyed_minions)

    return max_destroyed_minions

# Read input values
n, m, r = [int(x) for x in input().split()]
villages = []
minions = []

for _ in range(n):
    vx, vy, vr = [int(x) for x in input().split()]
    villages.append((vx, vy, vr))

for _ in range(m):
    mx, my = [int(x) for x in input().split()]
    minions.append((mx, my))

result = find_max_destroyed_minions(n, m, r, villages, minions)
print(result)
```
