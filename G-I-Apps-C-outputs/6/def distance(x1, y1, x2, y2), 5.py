
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_visible(x1, y1, x2, y2, peaks):
    for peak in peaks:
        px, py, pr = peak
        d1 = distance(x1, y1, px, py)
        d2 = distance(x2, y2, px, py)
        if d1 <= pr and d2 <= pr:
            return False
    return True

def lit_beacons(beacons, peaks):
    messages = 0
    reachable = list(range(len(beacons)))

    for i in range(len(beacons)):
        for j in range(i+1, len(beacons)):
            if is_visible(beacons[i][0], beacons[i][1], beacons[j][0], beacons[j][1], peaks):
                if i in reachable:
                    reachable.remove(j)
    
    messages = len(reachable)
    return messages

n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
peaks = [tuple(map(int, input().split())) for _ in range(m)]

print(lit_beacons(beacons, peaks))
```
