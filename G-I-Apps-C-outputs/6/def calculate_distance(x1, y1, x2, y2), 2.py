
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def is_blocked(x1, y1, x2, y2, x_peak, y_peak, r_peak):
    distance = calculate_distance(x1, y1, x2, y2)
    return distance <= r_peak

def is_visible(x1, y1, x2, y2, peaks):
    for peak in peaks:
        x_peak, y_peak, r_peak = peak
        if is_blocked(x1, y1, x2, y2, x_peak, y_peak, r_peak):
            return False
    return True

def count_riders(beacons, peaks):
    total_riders = 0
    for beacon in beacons:
        x_beacon, y_beacon = beacon
        for other_beacon in beacons:
            if other_beacon != beacon:
                x_other, y_other = other_beacon
                if is_visible(x_beacon, y_beacon, x_other, y_other, peaks):
                    total_riders += 1
                    break
    return total_riders

n, m = map(int, input().split())
beacons = [list(map(int, input().split())) for _ in range(n)]
peaks = [list(map(int, input().split())) for _ in range(m)]

result = count_riders(beacons, peaks)
print(result)
```
