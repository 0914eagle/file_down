
import math

def can_attack(minion_x, minion_y, attack_center_x, attack_center_y, attack_radius):
    distance = math.sqrt((minion_x - attack_center_x) ** 2 + (minion_y - attack_center_y) ** 2)
    return distance <= attack_radius

def max_minions_destroyed(n, m, r, villages, minions):
    max_destroyed = 0

    for i in range(m):
        destroyed = 0
        minion_x, minion_y = minions[i]
        for j in range(n):
            village_x, village_y, village_r = villages[j]
            if can_attack(minion_x, minion_y, village_x, village_y, r - village_r):
                destroyed += 1
        max_destroyed = max(max_destroyed, destroyed)

    return max_destroyed

# Read input
n, m, r = map(int, input().split())
villages = [tuple(map(int, input().split())) for _ in range(n)]
minions = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and print output
print(max_minions_destroyed(n, m, r, villages, minions))
```
