
import math

def is_blocked(x1, y1, x2, y2, x3, y3, r):
    dist_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
    u = ((x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1)) / dist_squared
    if u < 0 or u > 1:
        return False
    x = x1 + u * (x2 - x1)
    y = y1 + u * (y2 - y1)
    if (x - x3) ** 2 + (y - y3) ** 2 <= r ** 2:
        return True
    return False

def count_messages(beacons, peaks):
    n = len(beacons)
    messages = 0
    lit = [False] * n
    lit[0] = True  # Start by lighting the first beacon

    while not all(lit):
        messages += 1
        for i in range(n):
            for j in range(n):
                if i != j and not lit[j] and not is_blocked(beacons[i][0], beacons[i][1], beacons[j][0], beacons[j][1], peaks[i][0], peaks[i][1], peaks[i][2]):
                    lit[j] = True

    return messages

# Read input
n, m = map(int, input().split())
beacons = [list(map(int, input().split())) for _ in range(n)]
peaks = [list(map(int, input().split())) for _ in range(m)]

# Calculate and output result
result = count_messages(beacons, peaks)
print(result)
```
