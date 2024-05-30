
import numpy as np

def slice_thickness(n, s, holes):
    cheese_density = 1.0  # Density of the cheese in g/cm^3
    cheese_volume = 100 * 100 * 100  # Volume of the cheese block in cm^3
    cheese_mass = cheese_density * cheese_volume  # Total mass of the cheese in grams

    hole_volumes = np.pi * np.power(holes[:, 0], 3) * 4 / 3  # Volumes of the holes in cm^3
    total_hole_volume = np.sum(hole_volumes)  # Total volume of the holes in cm^3

    remaining_mass = cheese_mass - total_hole_volume  # Mass of the cheese without holes in grams
    slice_mass = remaining_mass / s  # Mass of each slice in grams
    slice_volume = slice_mass / cheese_density  # Volume of each slice in cm^3
    slice_thickness = slice_volume / 10000  # Thickness of each slice in millimeters

    return [slice_thickness for _ in range(s)]

# Input
n, s = map(int, input().split())
holes = np.zeros((n, 4), dtype=int)
for i in range(n):
    holes[i] = list(map(int, input().split()))

# Output
slice_thicknesses = slice_thickness(n, s, holes)
for thickness in slice_thicknesses:
    print("{:.9f}".format(thickness))
```

