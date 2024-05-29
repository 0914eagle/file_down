
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_blocked(x1, y1, x2, y2, mountain_peaks):
    for peak in mountain_peaks:
        peak_x, peak_y, peak_r = peak
        d = abs((x2 - x1)*(peak_y - y1) - (y2 - y1)*(peak_x - x1)) / distance(x1, y1, x2, y2)
        if d < peak_r:
            return True
    return False

def solve(num_beacons, num_peaks, beacons, mountain_peaks):
    lit_beacons = set()
    messages = 0
    
    for beacon in beacons:
        x1, y1 = beacon
        for other_beacon in beacons:
            x2, y2 = other_beacon
            if (x1, y1) != (x2, y2) and not is_blocked(x1, y1, x2, y2, mountain_peaks):
                lit_beacons.add(other_beacon)
    
    while len(lit_beacons) < num_beacons:
        messages += 1
        new_lit_beacons = set()
        for beacon in lit_beacons:
            x1, y1 = beacon
            for other_beacon in beacons:
                x2, y2 = other_beacon
                if (x1, y1) != (x2, y2) and not is_blocked(x1, y1, x2, y2, mountain_peaks):
                    new_lit_beacons.add(other_beacon)
        lit_beacons |= new_lit_beacons
    
    return messages

n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
mountain_peaks = [tuple(map(int, input().split())) for _ in range(m)]

result = solve(n, m, beacons, mountain_peaks)
print(result)
```
