
import math

def calculate_slice_thickness(n, s, holes):
    total_volume = 100 * 100 * 100
    hole_volumes = [4/3 * math.pi * r**3 for r, _, _, _ in holes]
    total_holes_volume = sum(hole_volumes)
    remaining_volume = total_volume - total_holes_volume
    
    slice_thickness = remaining_volume / s / (100 * 100)
    return [slice_thickness] * s

# Input parsing
n, s = map(int, input().split())
holes = []
for _ in range(n):
    r, x, y, z = map(int, input().split())
    holes.append((r, x, y, z))

# Calculate and output slice thicknesses
slice_thicknesses = calculate_slice_thickness(n, s, holes)
for thickness in slice_thicknesses:
    print("{:.9f}".format(thickness))

# Example input
# 0 4
# Example output
# 25.000000000
# 25.000000000
# 25.000000000
# 25.000000000
```
