
import math

def euclidean_circle_area(radius):
    return math.pi * radius**2

def taxicab_circle_area(radius):
    return 2 * radius**2

# Input
radius = int(input())

# Output
print(f"{euclidean_circle_area(radius):.6f}")
print(f"{taxicab_circle_area(radius):.6f}")
```
