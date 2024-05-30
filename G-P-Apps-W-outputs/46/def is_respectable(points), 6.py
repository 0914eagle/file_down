
def is_respectable(points):
    x_values = set()
    y_values = set()
    
    for point in points:
        x_values.add(point[0])
        y_values.add(point[1])
    
    if len(x_values) != 3 or len(y_values) != 3:
        return "ugly"
    
    x_values = sorted(list(x_values))
    y_values = sorted(list(y_values))
    
    if (x_values[0], y_values[0]) == points[4] and (x_values[1], y_values[1]) == points[5] and (x_values[2], y_values[2]) == points[7]:
        return "ugly"
    
    return "respectable"

points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

print(is_respectable(points))
```
