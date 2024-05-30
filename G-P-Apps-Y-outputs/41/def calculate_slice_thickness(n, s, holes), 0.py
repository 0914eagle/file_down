
import math

def calculate_slice_thickness(n, s, holes):
    cheese_volume = 100 * 100 * 100 * 1000  # Convert to cubic millimeters
    total_hole_volume = sum(4/3 * math.pi * r**3 for r, _, _, _ in holes)
    
    for i in range(1, s + 1):
        volume_sliced = cheese_volume / s * i
        remaining_cheese_volume = cheese_volume - total_hole_volume - volume_sliced
        thickness = remaining_cheese_volume / (100 * 100)  # Slice area is 100x100 mm
        print("{:.9f}".format(thickness / 1000))  # Convert to millimeters

# Example usage
n = 0
s = 4
holes = []
calculate_slice_thickness(n, s, holes)
```

This function calculates the thickness of each slice to ensure they have equal weight. The input parameters `n`, `s`, and `holes` correspond to the number of holes in the cheese, the number of slices to cut, and the details of the holes respectively. The function then calculates the thickness of each slice and prints it out.

You can modify the input parameters to test the function with different scenarios. Let me know if you have any questions or need further assistance! 