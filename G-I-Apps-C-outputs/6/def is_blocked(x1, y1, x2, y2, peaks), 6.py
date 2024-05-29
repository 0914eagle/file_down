
import math

def is_blocked(x1, y1, x2, y2, peaks):
    for peak in peaks:
        px, py, pr = peak
        dist_sq = (x2 - x1)**2 + (y2 - y1)**2
        dot = ((x2 - x1) * (px - x1)) + ((y2 - y1) * (py - y1))
        closest_x = x1 + (((px - x1) * dot) / dist_sq)
        closest_y = y1 + (((py - y1) * dot) / dist_sq)
        
        if dot < 0:
            closest_x = x1
            closest_y = y1
        elif dot > dist_sq:
            closest_x = x2
            closest_y = y2
        
        if math.sqrt((px - closest_x)**2 + (py - closest_y)**2) < pr:
            return True
    
    return False

def lit_beacons(beacons, peaks):
    messages = 0
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in range(len(beacons)):
            if neighbor not in visited and not is_blocked(beacons[node][0], beacons[node][1], beacons[neighbor][0], beacons[neighbor][1], peaks):
                dfs(neighbor)
    
    for i in range(len(beacons)):
        if i not in visited:
            messages += 1
            dfs(i)

    return messages

# Read input
n, m = map(int, input().split())
beacons = [list(map(int, input().split())) for _ in range(n)]
peaks = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print the number of messages
print(lit_beacons(beacons, peaks))
```
