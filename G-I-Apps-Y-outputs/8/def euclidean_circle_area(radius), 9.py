
import math

# Function to calculate the area of a circle in Euclidian geometry
def euclidean_circle_area(radius):
    return math.pi * radius**2

# Function to calculate the area of a circle in taxicab geometry
def taxicab_circle_area(radius):
    return 2 * radius**2

# Read the radius input
radius = int(input())

# Calculate and output the areas of the circles in both geometries
print(f"{euclidean_circle_area(radius):.6f}")
print(f"{taxicab_circle_area(radius):.6f}")
```
