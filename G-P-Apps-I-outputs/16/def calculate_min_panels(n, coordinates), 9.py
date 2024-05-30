
def calculate_min_panels(n, coordinates):
    panels = 6 * n
    for coord in coordinates:
        x, y, z = coord
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
coordinates = []
for _ in range(n):
    x, y, z = map(int, input().split())
    coordinates.append((x, y, z))

# Calculate and output result
print(calculate_min_panels(n, coordinates))
```
