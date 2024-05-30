
import math

def max_pickles_on_sandwich(s, r, n, z):
    max_area_covered = (z / 100) * math.pi * s**2
    pickle_area = n * math.pi * r**2
    max_pickles = min(n, math.floor(max_area_covered / pickle_area))
    return max_pickles

# Read input
s, r = map(float, input().split())
n, z = map(int, input().split())

# Calculate and output the result
result = max_pickles_on_sandwich(s, r, n, z)
print(result)
```
