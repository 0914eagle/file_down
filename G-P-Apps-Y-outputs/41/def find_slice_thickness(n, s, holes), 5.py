
import math

def find_slice_thickness(n, s, holes):
    total_volume = 100 * 100 * 100 * (100 * 100 * 100 - n * (4/3) * math.pi * (r**3 for r, _, _, _ in holes))
    slice_weight = total_volume / s
    slice_thickness = slice_weight / (100 * 100)
    
    return [slice_thickness] * s

# Sample Input
n = 0
s = 4
holes = []

# Sample Output
output = find_slice_thickness(n, s, holes)
for thickness in output:
    print("{:.9f}".format(thickness))

```

