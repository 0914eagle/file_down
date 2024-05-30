
def min_panels_to_contain_defective_cells(n, defective_cells):
    if n == 0:
        return 0
    
    panels = 6 * n  # Each defective cell requires 6 panels
    
    for cell in defective_cells:
        x, y, z = cell
        if x == 0:
            panels -= 1
        if x == 9:
            panels -= 1
        if y == 0:
            panels -= 1
        if y == 9:
            panels -= 1
        if z == 0:
            panels -= 1
        if z == 9:
            panels -= 1
    
    return panels

# Read input
n = int(input())
defective_cells = []
for _ in range(n):
    x, y, z = map(int, input().split())
    defective_cells.append((x, y, z))

# Calculate and output result
result = min_panels_to_contain_defective_cells(n, defective_cells)
print(result)
```
