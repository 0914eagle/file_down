
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def can_destroy(minion_x, minion_y, minion_r, village_x, village_y, village_r, radius):
    minion_distance = calculate_distance(minion_x, minion_y, village_x, village_y)
    return minion_distance - minion_r > radius - village_r

def max_destroyed(n, m, r, villages, minions):
    max_destroyed_count = 0
    for minion_x, minion_y in minions:
        destroyed_count = 0
        for village_x, village_y, village_r in villages:
            if can_destroy(minion_x, minion_y, 0, village_x, village_y, village_r, r):
                destroyed_count += 1
        if destroyed_count == n:
            max_destroyed_count = max(max_destroyed_count, m)

    return max_destroyed_count

# Input parsing
n, m, r = map(int, input().split())
villages = [tuple(map(int, input().split())) for _ in range(n)]
minions = [tuple(map(int, input().split())) for _ in range(m)]

print(max_destroyed(n, m, r, villages, minions))
```
