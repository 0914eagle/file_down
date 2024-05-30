
def min_panels_to_contain_defective_cells():
    n = int(input())
    defective_cells = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        defective_cells.append((x, y, z))

    panels_required = 6 * n
    for cell in defective_cells:
        x, y, z = cell
        if x == 0:
            panels_required += 1
        if x == 9:
            panels_required += 1
        if y == 0:
            panels_required += 1
        if y == 9:
            panels_required += 1
        if z == 0:
            panels_required += 1
        if z == 9:
            panels_required += 1

    print(panels_required)

min_panels_to_contain_defective_cells()
```
