
import math

def can_hit_village(cx, cy, r, vx, vy, vr):
    if (cx - vx) ** 2 + (cy - vy) ** 2 <= (r - vr) ** 2:
        return True
    return False

def count_destroyed_minions(villages, minions, r):
    max_destroyed = 0
    for cx, cy, _ in villages:
        destroyed = sum(1 for mx, my in minions if math.sqrt((cx - mx) ** 2 + (cy - my) ** 2) <= r)
        for vx, vy, vr in villages:
            if can_hit_village(cx, cy, r, vx, vy, vr):
                destroyed -= 1
        max_destroyed = max(max_destroyed, destroyed)
    return max_destroyed

def solve_game():
    n, m, r = map(int, input().split())
    villages = [list(map(int, input().split())) for _ in range(n)]
    minions = [tuple(map(int, input().split())) for _ in range(m)]

    max_destroyed = count_destroyed_minions(villages, minions, r)
    print(max_destroyed)

solve_game()
```
