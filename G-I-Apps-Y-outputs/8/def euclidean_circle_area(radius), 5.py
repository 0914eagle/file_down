
import math

def euclidean_circle_area(radius):
    return math.pi * radius**2

def taxicab_circle_area(radius):
    return 2 * radius**2

radius = int(input())
euclidean_area = euclidean_circle_area(radius)
taxicab_area = taxicab_circle_area(radius)

print(f"{euclidean_area:.6f}")
print(f"{taxicab_area:.6f}")
```
