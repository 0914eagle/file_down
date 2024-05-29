
import math

def is_inside_circle(x, y, cx, cy, r):
    return (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

def maximum_minions_destroyed(n, m, r, villages, minions):
    max_destroyed = 0

    for x, y in minions:
        count = 0
        for vx, vy, vr in villages:
            if is_inside_circle(x, y, vx, vy, vr):
                count = 0
                break
            elif math.sqrt((x - vx) ** 2 + (y - vy) ** 2) <= r:
                count += 1
        max_destroyed = max(max_destroyed, count)
    
    return max_destroyed

# Input processing and function call
n, m, r = map(int, input().split())
villages = [list(map(int, input().split())) for _ in range(n)]
minions = [list(map(int, input().split())) for _ in range(m)]

result = maximum_minions_destroyed(n, m, r, villages, minions)
print(result)
```
