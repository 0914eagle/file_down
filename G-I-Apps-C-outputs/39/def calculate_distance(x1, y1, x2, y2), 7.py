
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def max_minions_destroyed(n, m, r, villages, minions):
    max_destroyed = 0
    for x_center in range(-20000, 20001):
        for y_center in range(-20000, 20001):
            destroyed = 0
            for minion in minions:
                if all(calculate_distance(x_center, y_center, minion[0], minion[1]) <= r for village in villages if calculate_distance(x_center, y_center, village[0], village[1]) - village[2] > r):
                    destroyed += 1
            max_destroyed = max(max_destroyed, destroyed)
    return max_destroyed

# Reading input
n, m, r = map(int, input().split())
villages = [tuple(map(int, input().split())) for _ in range(n)]
minions = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate the maximum number of minions Liam can destroy in a single attack
result = max_minions_destroyed(n, m, r, villages, minions)
print(result)
```
