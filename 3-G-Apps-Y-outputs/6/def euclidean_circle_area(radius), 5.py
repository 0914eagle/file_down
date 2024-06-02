
import math

def euclidean_circle_area(radius):
    return math.pi * radius**2

def taxicab_circle_area(radius):
    return 2 * radius**2

# Input
radius = int(input())

# Output
print('{:.6f}'.format(euclidean_circle_area(radius)))
print('{:.6f}'.format(taxicab_circle_area(radius)))
