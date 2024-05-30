
import math

def max_pickles_on_sandwich(s, r, n, z):
    total_area = math.pi * s**2
    pickle_area = n * math.pi * r**2
    max_pickle_area = z/100 * total_area
    
    max_pickles = min(n, math.floor(max_pickle_area / (math.pi * r**2)))
    
    return max_pickles

# Input processing
s, r = map(float, input().split())
n, z = map(int, input().split())

# Call the function and print the result
print(max_pickles_on_sandwich(s, r, n, z))
```
