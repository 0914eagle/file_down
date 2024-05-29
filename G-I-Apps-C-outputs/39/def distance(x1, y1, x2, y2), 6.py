
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def can_attack(x, y, r, villages, minions):
    for vx, vy, vr in villages:
        if distance(x, y, vx, vy) - vr < r:
            return False
    for mx, my in minions:
        if distance(x, y, mx, my) < r:
            return True
    return False

def max_destroyed_villages(n, m, r, villages, minions):
    max_count = 0
    for mx, my in minions:
        count = sum(can_attack(mx, my, r, villages, minions) for mx, my in minions)
        max_count = max(max_count, count)
    return max_count

# Read input
n, m, r = map(int, input().split())
villages = [list(map(int, input().split())) for _ in range(n)]
minions = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print output
print(max_destroyed_villages(n, m, r, villages, minions))
```
