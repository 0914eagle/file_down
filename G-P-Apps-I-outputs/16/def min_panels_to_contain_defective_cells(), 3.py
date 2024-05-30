
def min_panels_to_contain_defective_cells():
    n = int(input())
    cells = [tuple(map(int, input().split())) for _ in range(n)]

    panels = 0
    for cell in cells:
        x, y, z = cell

        # Count panels needed for each face of the cell
        panels += 6

        # Check if adjacent cells exist on each face
        if (x-1, y, z) not in cells:
            panels += 1
        if (x+1, y, z) not in cells:
            panels += 1
        if (x, y-1, z) not in cells:
            panels += 1
        if (x, y+1, z) not in cells:
            panels += 1
        if (x, y, z-1) not in cells:
            panels += 1
        if (x, y, z+1) not in cells:
            panels += 1

    return panels

print(min_panels_to_contain_defective_cells())
```
