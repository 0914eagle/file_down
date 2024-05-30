
def min_panels_to_contain_defective_cells(n, defective_cells):
    if n == 0:
        return 0
    
    total_panels = 0
    for cell in defective_cells:
        x, y, z = cell
        panels = 6
        if x == 0 or x == 9:
            panels -= 1
        if y == 0 or y == 9:
            panels -= 1
        if z == 0 or z == 9:
            panels -= 1
        total_panels += panels
    
    return total_panels

# Read input
n = int(input())
defective_cells = []
for _ in range(n):
    cell = tuple(map(int, input().split()))
    defective_cells.append(cell)

# Output result
print(min_panels_to_contain_defective_cells(n, defective_cells))
```
