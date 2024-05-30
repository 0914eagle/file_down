
def find_inner_point(n, points):
    boundary_points = set()
    
    for x, y in points:
        if x == 0 or x == 2 or y == 0 or y == 2:
            boundary_points.add((x, y))
    
    for x, y in points:
        if (x, y) not in boundary_points:
            return x, y

# Read input
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(4*n + 1)]

# Find inner point and print output
inner_point = find_inner_point(n, points)
print(inner_point[0], inner_point[1])
```
