
import math

def solve(opponents):
    max_hits = 0
    for angle in range(360):
        hits = 0
        for x, y, r in opponents:
            dx = x - 0
            dy = y - 0
            distance = math.sqrt(dx**2 + dy**2)
            if distance < r:
                continue
            angle_to_center = math.degrees(math.atan2(dy, dx))
            angle_to_center = (angle_to_center + 360) % 360
            if abs(angle - angle_to_center) < 1e-9:
                hits += 1
        max_hits = max(max_hits, hits)
    
    return max_hits

n = int(input())
opponents = []
for _ in range(n):
    x, y, r = map(float, input().split())
    opponents.append((x, y, r))

print(solve(opponents))

