
import math

def get_angle(x, y):
    return math.atan2(y, x)

def get_hit_count(opponents, angle):
    hit_count = 0
    for x, y, r in opponents:
        dx = x - math.cos(angle)
        dy = y - math.sin(angle)
        if dx * dx + dy * dy < r * r:
            hit_count += 1
    return hit_count

n = int(input())
opponents = []
for _ in range(n):
    x, y, r = map(float, input().split())
    opponents.append((x, y, r))

left = 0
right = math.pi * 2
while right - left > 1e-9:
    mid = (left + right) / 2
    if get_hit_count(opponents, mid) > get_hit_count(opponents, left):
        left = mid
    else:
        right = mid

print(get_hit_count(opponents, left))

