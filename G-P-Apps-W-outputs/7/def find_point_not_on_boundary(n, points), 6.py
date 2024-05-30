
def find_point_not_on_boundary(n, points):
    boundary_points = set()
    
    for x, y in points:
        if x == 0 or x == 2 or y == 0 or y == 2:
            boundary_points.add((x, y))
    
    for x, y in points:
        if (x, y) not in boundary_points:
            return x, y

# Input parsing
n = int(input())
points = []
for _ in range(4*n + 1):
    x, y = map(int, input().split())
    points.append((x, y))

# Output
result = find_point_not_on_boundary(n, points)
print(result[0], result[1])
```
