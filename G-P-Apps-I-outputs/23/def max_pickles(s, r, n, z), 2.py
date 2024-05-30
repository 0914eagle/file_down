
import math

def max_pickles(s, r, n, z):
    max_area = math.pi * s**2 * z / 100
    pickle_area = n * math.pi * r**2
    return min(n, math.floor(max_area / pickle_area))

# Read input
s, r = map(float, input().split())
n, z = map(int, input().split())

# Call the function and print the result
print(max_pickles(s, r, n, z))
```
