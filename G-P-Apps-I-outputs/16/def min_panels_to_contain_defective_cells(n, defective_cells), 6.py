
def min_panels_to_contain_defective_cells(n, defective_cells):
    panels = 6 * n  # 6 panels per defective cell
    
    # Check for panels needed for adjacent sides
    for cell in defective_cells:
        x, y, z = cell
        if (x-1, y, z) not in defective_cells:
            panels += 1
        if (x+1, y, z) not in defective_cells:
            panels += 1
        if (x, y-1, z) not in defective_cells:
            panels += 1
        if (x, y+1, z) not in defective_cells:
            panels += 1
        if (x, y, z-1) not in defective_cells:
            panels += 1
        if (x, y, z+1) not in defective_cells:
            panels += 1
    
    return panels

# Read input
n = int(input())
defective_cells = []
for _ in range(n):
    x, y, z = map(int, input().split())
    defective_cells.append((x, y, z))

# Calculate and output result
print(min_panels_to_contain_defective_cells(n, defective_cells))
```
