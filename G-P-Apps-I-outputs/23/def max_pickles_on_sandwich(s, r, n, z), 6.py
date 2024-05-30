
import math

def max_pickles_on_sandwich(s, r, n, z):
    sandwich_area = math.pi * s**2
    pickle_area = math.pi * r**2
    max_pickle_area = (z / 100) * sandwich_area
    
    if pickle_area * n <= max_pickle_area:
        return n
    
    max_pickles = 0
    remaining_area = max_pickle_area
    while n > 0 and remaining_area >= pickle_area:
        max_pickles += 1
        remaining_area -= pickle_area
        n -= 1

    return max_pickles

# Input parsing
s, r = map(float, input().split())
n, z = map(int, input().split())

# Output
print(max_pickles_on_sandwich(s, r, n, z))
```
