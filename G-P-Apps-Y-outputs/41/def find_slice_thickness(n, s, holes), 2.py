
import math

def find_slice_thickness(n, s, holes):
    total_volume = 100 * 100 * 100  # Total volume of the cheese block
    hole_volumes = []  # List to store volumes of each hole
    for hole in holes:
        r, x, y, z = hole
        volume = (4/3) * math.pi * r**3  # Volume of a sphere
        hole_volumes.append(volume)

    remaining_volume = total_volume - sum(hole_volumes)  # Remaining volume after removing holes
    slice_thickness = remaining_volume / s  # Thickness of each slice
    
    return slice_thickness

# Input processing
n, s = map(int, input().split())
holes = []
for _ in range(n):
    r, x, y, z = map(int, input().split())
    holes.append((r, x, y, z))

# Output
slice_thicknesses = find_slice_thickness(n, s, holes)
for _ in range(s):
    print("{:.9f}".format(slice_thicknesses))

```
