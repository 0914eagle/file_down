
import math

def are_beacons_within_sight(beacon1, beacon2, mountain_peaks):
    for peak in mountain_peaks:
        x1, y1 = beacon1
        x2, y2 = beacon2
        x3, y3, r = peak
        
        det = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
        if det == 0:  # Beacons are collinear
            return False
        
        lam = ((y3 - y1) * (x3 - x1) - (x3 - x1) * (y1 - y1)) / det
        nu = ((y2 - y1) * (x2 - x1) - (x2 - x1) * (y1 - y1)) / det
        
        if lam > 0 and lam < 1 and nu > 0 and nu < 1:
            return False
    
    return True

def count_messages(n, m, beacons, mountain_peaks):
    messages = 0
    lit_beacons = set()
    
    for beacon in beacons:
        if not lit_beacons.issuperset(set([beacon])):
            lit_beacons.add(beacon)
            messages += 1
            
            for next_beacon in beacons:
                if are_beacons_within_sight(beacon, next_beacon, mountain_peaks):
                    lit_beacons.add(next_beacon)
    
    return messages

# Read input
n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
mountain_peaks = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and print output
print(count_messages(n, m, beacons, mountain_peaks))
```
