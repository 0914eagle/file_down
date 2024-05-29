
import math

def is_blocked(x1, y1, x2, y2, x_peak, y_peak, r_peak):
    dx = x2 - x1
    dy = y2 - y1
    dist = math.hypot(dx, dy)
    
    if dist == 0:
        return False
    
    t = r_peak / dist
    ex = x1 + t * dx
    ey = y1 + t * dy
    
    if (ex - x_peak) ** 2 + (ey - y_peak) ** 2 <= r_peak ** 2:
        return True
    
    return False

def messages_to_send(n, m, beacons, peaks):
    messages = 0
    
    for i in range(n):
        for j in range(i+1, n):
            blocked = False
            for k in range(m):
                x_peak, y_peak, r_peak = peaks[k]
                if is_blocked(beacons[i][0], beacons[i][1], beacons[j][0], beacons[j][1], x_peak, y_peak, r_peak):
                    blocked = True
                    break
            if blocked:
                messages += 1
    
    return messages

# Input parsing
n, m = map(int, input().split())
beacons = [list(map(int, input().split())) for _ in range(n)]
peaks = [list(map(int, input().split())) for _ in range(m)]

result = messages_to_send(n, m, beacons, peaks)
print(result)
```
