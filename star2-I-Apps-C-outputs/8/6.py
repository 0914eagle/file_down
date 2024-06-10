
import math

def solve(n, circles):
    max_hits = 0
    for angle in range(0, 360):
        hits = 0
        for x, y, r in circles:
            if x * math.cos(math.radians(angle)) + y * math.sin(math.radians(angle)) < r:
                hits += 1
        max_hits = max(max_hits, hits)
    return max_hits

n = int(input())
circles = []
for _ in range(n):
    x, y, r = map(float, input().split())
    circles.append((x, y, r))

print(solve(n, circles))

