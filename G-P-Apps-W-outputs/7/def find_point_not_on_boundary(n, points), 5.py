
def find_point_not_on_boundary(n, points):
    count_x = {}
    count_y = {}
    
    for x, y in points:
        count_x[x] = count_x.get(x, 0) + 1
        count_y[y] = count_y.get(y, 0) + 1
        
    for x, y in points:
        if count_x[x] != 2 or count_y[y] != 2:
            return x, y

# Read input
n = int(input())
points = []
for _ in range(4*n + 1):
    x, y = map(int, input().split())
    points.append((x, y))

# Find and print the point not on the boundary
result = find_point_not_on_boundary(n, points)
print(*result)
```
