
import math

def euclidean_circle_area(r):
    return math.pi * r**2

def taxicab_circle_area(r):
    return 2 * r * r

# Taking input
r = int(input())

# Calculating and printing the areas
print(euclidean_circle_area(r))
print(taxicab_circle_area(r))
```
