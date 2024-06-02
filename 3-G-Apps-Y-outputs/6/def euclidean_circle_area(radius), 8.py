
import math

def euclidean_circle_area(radius):
    return math.pi * radius**2

def taxicab_circle_area(radius):
    return 2 * radius**2

# Read input
radius = int(input())

# Calculate and output areas
print(euclidean_circle_area(radius))
print(taxicab_circle_area(radius))
