
def find_point_not_on_boundary(n, points):
    x_count = {}
    y_count = {}
    
    for x, y in points:
        if x in x_count:
            x_count[x] += 1
        else:
            x_count[x] = 1
        
        if y in y_count:
            y_count[y] += 1
        else:
            y_count[y] = 1
    
    for x, count in x_count.items():
        if count % 2 != 0:
            unique_x = x

    for y, count in y_count.items():
        if count % 2 != 0:
            unique_y = y
            
    return unique_x, unique_y

n = int(input())
points = []
for _ in range(4*n + 1):
    x, y = map(int, input().split())
    points.append((x, y))

result = find_point_not_on_boundary(n, points)
print(result[0], result[1])
```
