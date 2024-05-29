
import math

def euclidean_circle_area(r):
    return math.pi * r**2

def taxicab_circle_area(r):
    return 2 * r**2

R = int(input())
print('{:.6f}'.format(euclidean_circle_area(R)))
print('{:.6f}'.format(taxicab_circle_area(R)))
```
