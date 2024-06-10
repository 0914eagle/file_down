
import math

def solve(opponents):
    n = len(opponents)
    angles = [0] * n
    for i in range(n):
        x, y, r = opponents[i]
        angles[i] = math.atan2(y, x)
    
    angles.sort()
    
    max_hits = 0
    for i in range(n):
        angle = angles[i]
        hits = 1
        for j in range(i + 1, n):
            if angles[j] - angle > math.pi:
                break
            hits += 1
        
        max_hits = max(max_hits, hits)
    
    return max_hits

n = int(input())
opponents = []
for _ in range(n):
    x, y, r = map(float, input().split())
    opponents.append((x, y, r))

print(solve(opponents))

