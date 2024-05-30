
import sys

def calculate_slice_thickness(n, s, holes):
    total_volume = 100 * 100 * 100
    hole_volumes = [4/3 * 3.141592653589793 * r**3 for r, _, _, _ in holes]
    cheese_volume = total_volume - sum(hole_volumes)
    slice_weight = cheese_volume / s

    slice_thicknesses = []
    current_slice_weight = slice_weight
    for i in range(s):
        remaining_cheese_volume = cheese_volume
        for r, _, _, _ in holes:
            hole_volume = 4/3 * 3.141592653589793 * r**3
            if hole_volume >= current_slice_weight:
                remaining_cheese_volume -= current_slice_weight
            else:
                remaining_cheese_volume -= hole_volume

        slice_thickness = remaining_cheese_volume / 10000
        slice_thicknesses.insert(0, slice_thickness)
        current_slice_weight += slice_weight

    return slice_thicknesses

if __name__ == "__main__":
    input_lines = sys.stdin.readlines()
    n, s = map(int, input_lines[0].strip().split())
    holes = [list(map(int, line.strip().split())) for line in input_lines[1:]]

    slice_thicknesses = calculate_slice_thickness(n, s, holes)
    for thickness in slice_thicknesses:
        print("{:.9f}".format(thickness))
```
