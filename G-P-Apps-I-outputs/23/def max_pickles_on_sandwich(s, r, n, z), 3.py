
import math

def max_pickles_on_sandwich(s, r, n, z):
    max_area_covered = math.pi * r**2 * n
    max_allowed_area = math.pi * s**2 * z / 100
    max_pickles = min(n, max_allowed_area / (math.pi * r**2))

    return int(max_pickles)

# Input
s, r = map(float, input().split())
n, z = map(int, input().split())

# Output
print(max_pickles_on_sandwich(s, r, n, z))
```
