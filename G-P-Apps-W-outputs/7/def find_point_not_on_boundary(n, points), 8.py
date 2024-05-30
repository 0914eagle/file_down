
def find_point_not_on_boundary(n, points):
    all_x = set()
    all_y = set()
    
    for x, y in points:
        all_x.add(x)
        all_y.add(y)
    
    boundary_x = set()
    boundary_y = set()
    
    for x, y in points:
        if list(all_x).count(x) == 1 or list(all_y).count(y) == 1:
            return x, y

# Read input
n = int(input())
points = []
for _ in range(4*n + 1):
    x, y = map(int, input().split())
    points.append((x, y))

# Find and print the point not on the boundary
result = find_point_not_on_boundary(n, points)
print(result[0], result[1])
```
