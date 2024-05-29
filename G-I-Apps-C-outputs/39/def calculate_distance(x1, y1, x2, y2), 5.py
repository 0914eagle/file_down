
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def can_attack(xa, ya, xv, yv, vr, r):
    d = calculate_distance(xa, ya, xv, yv)
    return d <= r - vr

def max_destroyed_minions(n, m, r, villages, minions):
    max_minions_destroyed = 0
    
    for xa, ya in minions:
        destroyed_minions = 0
        for xv, yv, vr in villages:
            if can_attack(xa, ya, xv, yv, vr, r):
                destroyed_minions += 1
        max_minions_destroyed = max(max_minions_destroyed, destroyed_minions)
    
    return max_minions_destroyed

# Read input
n, m, r = map(int, input().split())
villages = [list(map(int, input().split())) for _ in range(n)]
minions = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print output
print(max_destroyed_minions(n, m, r, villages, minions))
```
