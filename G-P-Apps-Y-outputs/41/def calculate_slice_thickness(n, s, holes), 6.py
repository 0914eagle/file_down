
import math

def calculate_slice_thickness(n, s, holes):
    total_volume = 100 * 100 * 100 * (100 * 100)  # Total volume of cheese without holes
    hole_volumes = [4/3 * math.pi * r**3 for r, _, _, _ in holes]
    
    for r, _, _, _ in holes:
        total_volume -= 4/3 * math.pi * r**3
    
    slice_weight = total_volume / s
    slice_thicknesses = []
    
    current_slice_weight = 0
    current_thickness = 100
    for r, _, _, _ in holes:
        current_slice_weight += 4/3 * math.pi * r**3
        while current_slice_weight >= slice_weight:
            current_slice_weight -= slice_weight
            slice_thicknesses.append(round(current_thickness, 9))
            current_thickness = 100
            
        remaining_volume = slice_weight - current_slice_weight
        current_thickness = 2 * (math.sqrt(25 * 25 - (25 - math.sqrt(25 * 25 - remaining_volume / (100 * 100)))**2))
    slice_thicknesses.append(round(current_thickness, 9))
    
    while len(slice_thicknesses) < s:
        slice_thicknesses.append(0)
    
    return slice_thicknesses

# Input
n, s = map(int, input().split())
holes = []
for _ in range(n):
    r, x, y, z = map(int, input().split())
    holes.append((r, x, y, z))

# Output
result = calculate_slice_thickness(n, s, holes)
for thickness in result:
    print(thickness)
