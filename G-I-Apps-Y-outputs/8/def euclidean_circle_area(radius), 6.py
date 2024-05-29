
import math

# Function to calculate the area of a circle in Euclidian geometry
def euclidean_circle_area(radius):
    return math.pi * radius * radius

# Function to calculate the area of a circle in taxicab geometry
def taxicab_circle_area(radius):
    return 2 * radius * radius

# Read input
radius = int(input())

# Calculate and print the areas of the circles
print(euclidean_circle_area(radius))
print(taxicab_circle_area(radius))
```
