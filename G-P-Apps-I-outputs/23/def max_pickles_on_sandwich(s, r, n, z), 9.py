
import math

def max_pickles_on_sandwich(s, r, n, z):
    sandwich_area = math.pi * s**2
    pickle_area = math.pi * r**2
    max_pickle_area = (z / 100) * sandwich_area
    max_pickles = min(n, math.floor(max_pickle_area / pickle_area))
    return max_pickles

# Input
s, r = map(float, input().split())
n, z = map(int, input().split())

# Output
print(max_pickles_on_sandwich(s, r, n, z))
```
