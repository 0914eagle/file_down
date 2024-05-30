
import math

def slice_thickness(n, s, holes):
    total_volume = 100 * 100 * 100
    total_weight = total_volume - sum(math.pi * r**2 for r, _, _, _ in holes)
    slice_weight = total_weight / s
    slice_thickness = slice_weight / (100 * 100)

    return [slice_thickness for _ in range(s)]

# Input parsing
n, s = map(int, input().split())
holes = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and output slice thicknesses
slice_thicknesses = slice_thickness(n, s, holes)
for thickness in slice_thicknesses:
    print("{:.9f}".format(thickness))

```
