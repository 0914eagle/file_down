
def minimum_panels(n, defective_cells):
    if n == 0:
        return 0
    panels = n * 6
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

# Call the function and print the output
print(minimum_panels(n, defective_cells))
```
