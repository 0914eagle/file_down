
import math

def is_blocked(x1, y1, x2, y2, mountains):
    for mountain in mountains:
        mx, my, r = mountain
        if ((x1-mx)**2 + (y1-my)**2 <= r**2) and ((x2-mx)**2 + (y2-my)**2 <= r**2):
            return True
    return False

def count_messages(beacons, mountains):
    n = len(beacons)
    messages = 0
    
    reachable = [True] * n
    for i in range(n):
        for j in range(i+1, n):
            if is_blocked(beacons[i][0], beacons[i][1], beacons[j][0], beacons[j][1], mountains):
                reachable[j] = False
    
    for i in range(n):
        if reachable[i]:
            messages += 1
            for j in range(i+1, n):
                if is_blocked(beacons[i][0], beacons[i][1], beacons[j][0], beacons[j][1], mountains):
                    reachable[j] = False
    
    return messages

n, m = map(int, input().split())
beacons = []
mountains = []
for _ in range(n):
    x, y = map(int, input().split())
    beacons.append((x, y))
    
for _ in range(m):
    x, y, r = map(int, input().split())
    mountains.append((x, y, r))

print(count_messages(beacons, mountains))
```
