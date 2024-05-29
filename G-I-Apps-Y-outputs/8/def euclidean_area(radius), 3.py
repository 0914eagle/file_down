
import math

def euclidean_area(radius):
    return math.pi * radius**2

def taxicab_area(radius):
    return 2 * radius**2

# Input
radius = int(input().strip())

# Calculate and output areas
euclidean_radius = euclidean_area(radius)
taxicab_radius = taxicab_area(radius)

print(f"{euclidean_radius:.6f}")
print(f"{taxicab_radius:.6f}")
```
