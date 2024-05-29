
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def is_blocked(x1, y1, x2, y2, mountain_peaks):
    for peak in mountain_peaks:
        peak_x, peak_y, peak_r = peak
        dist_a = distance(x1, y1, peak_x, peak_y)
        dist_b = distance(x2, y2, peak_x, peak_y)
        if dist_a <= peak_r and dist_b <= peak_r:
            return True
    return False

def num_messages(n, m, beacons, mountain_peaks):
    messages = 0
    for i in range(n):
        for j in range(i + 1, n):
            if not is_blocked(beacons[i][0], beacons[i][1], beacons[j][0], beacons[j][1], mountain_peaks):
                messages += 1
    return messages

n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
mountain_peaks = [tuple(map(int, input().split())) for _ in range(m)]

result = num_messages(n, m, beacons, mountain_peaks)
print(result)
```
