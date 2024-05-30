
import math

def max_pickles_on_sandwich(s, r, n, z):
    total_area = math.pi * s**2
    pickle_area = math.pi * r**2
    max_pickle_area = total_area * z / 100

    max_pickles = min(n, int(max_pickle_area / pickle_area))
    return max_pickles

# Input
s, r = map(float, input().split())
n, z = map(int, input().split())

# Output
print(max_pickles_on_sandwich(s, r, n, z))
```
