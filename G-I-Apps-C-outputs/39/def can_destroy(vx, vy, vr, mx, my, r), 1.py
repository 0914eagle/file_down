
import math

def can_destroy(vx, vy, vr, mx, my, r):
    distance = math.sqrt((mx - vx)**2 + (my - vy)**2)
    return distance - vr <= r

def max_minions_destroyed(n, m, r, villages, minions):
    max_destroyed = 0

    for x in range(0, 20001):
        for y in range(0, 20001):
            destroyed = sum(1 for vx, vy, vr in villages if all(can_destroy(vx, vy, vr, x, y, r)))
            max_destroyed = max(max_destroyed, destroyed)

    return max_destroyed

# Input parsing and function call
def solve_tower_game():
    n, m, r = map(int, input().split())
    villages = [tuple(map(int, input().split())) for _ in range(n)]
    minions = [tuple(map(int, input().split())) for _ in range(m)]

    result = max_minions_destroyed(n, m, r, villages, minions)
    print(result)

# Example usage
solve_tower_game()
