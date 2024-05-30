
def is_respectable(points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    
    x_values.sort()
    y_values.sort()
    
    x_center = x_values[1]
    y_center = y_values[1]
    
    for x in x_values:
        for y in y_values:
            if (x != x_center or y != y_center) and (x, y) not in points:
                return "ugly"
    
    return "respectable"

points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

print(is_respectable(points))
```
