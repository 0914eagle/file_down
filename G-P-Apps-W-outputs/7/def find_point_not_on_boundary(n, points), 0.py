
def find_point_not_on_boundary(n, points):
    boundary_points = set()
    
    # Add all boundary points to a set
    for i in range(n):
        boundary_points.add((points[i][0], points[i][1]))
        boundary_points.add((points[n + i][0], points[n + i][1]))
        boundary_points.add((points[2*n + i][0], points[2*n + i][1]))
        boundary_points.add((points[3*n + i][0], points[3*n + i][1]))
    
    # Find the point that is not on the boundary
    for point in points:
        if tuple(point) not in boundary_points:
            return point

# Input
n = int(input())
points = []
for _ in range(4*n + 1):
    x, y = map(int, input().split())
    points.append((x, y))

# Output
result = find_point_not_on_boundary(n, points)
print(result[0], result[1])
```
