
def identify_point(n, points):
    all_x = set()
    all_y = set()
    boundary_points = set()

    for point in points:
        x, y = point
        all_x.add(x)
        all_y.add(y)
        if x == 0 or x == 2 or y == 0 or y == 2:
            boundary_points.add((x, y))

    for point in points:
        if point not in boundary_points:
            return point

# Example usage
n = 2
points = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
result = identify_point(n, points)
print(result[0], result[1])
```
