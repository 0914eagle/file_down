
def find_point_not_on_boundary(n, points):
    x_count = {}
    y_count = {}
    
    for x, y in points:
        x_count[x] = x_count.get(x, 0) + 1
        y_count[y] = y_count.get(y, 0) + 1
    
    for x, count in x_count.items():
        if count % 2 != 0:
            unique_x = x
    
    for y, count in y_count.items():
        if count % 2 != 0:
            unique_y = y
            
    return unique_x, unique_y

# Input
n = int(input())
points = []
for _ in range(4*n + 1):
    x, y = map(int, input().split())
    points.append((x, y))

# Output
result = find_point_not_on_boundary(n, points)
print(result[0], result[1])
