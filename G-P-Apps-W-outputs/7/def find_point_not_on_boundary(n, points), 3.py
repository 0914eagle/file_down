
def find_point_not_on_boundary(n, points):
    point_count = {}
    for x, y in points:
        if (x, y) in point_count:
            point_count[(x, y)] += 1
        else:
            point_count[(x, y)] = 1
    
    for point, count in point_count.items():
        if count == 1:
            return point

# Input parsing
n = int(input())
points = []
for _ in range(4*n + 1):
    x, y = map(int, input().split())
    points.append((x, y))

# Find and output the point not on the boundary of the square
result = find_point_not_on_boundary(n, points)
print(result[0], result[1])
```
