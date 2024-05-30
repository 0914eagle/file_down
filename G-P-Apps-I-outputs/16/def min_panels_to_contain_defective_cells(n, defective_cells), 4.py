
def min_panels_to_contain_defective_cells(n, defective_cells):
    if n == 0:
        return 0

    total_panels = 0

    for cell in defective_cells:
        x, y, z = cell
        panels = 6  # Each cell needs at least 6 panels
        if x == 0:
            panels -= 1  # One less panel if the cell is at the edge in x-direction
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

        total_panels += panels

    return total_panels

# Input parsing
n = int(input())
defective_cells = []
for _ in range(n):
    coordinates = input().split()
    x, y, z = map(int, coordinates)
    defective_cells.append((x, y, z))

print(min_panels_to_contain_defective_cells(n, defective_cells))
```
