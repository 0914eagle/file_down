
import math

def euclidean_circle_area(radius):
    return math.pi * radius**2

def taxicab_circle_area(radius):
    return 2 * radius**2

def solve_circle_areas(radius):
    euclidean_area = euclidean_circle_area(radius)
    taxicab_area = taxicab_circle_area(radius)

    return euclidean_area, taxicab_area

radius = int(input())
euclidean_area, taxicab_area = solve_circle_areas(radius)
print(f"{euclidean_area:.6f}")
print(f"{taxicab_area:.6f}")
```
