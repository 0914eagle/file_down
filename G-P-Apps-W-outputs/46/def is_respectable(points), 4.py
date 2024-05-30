
def is_respectable(points):
    x_values = set()
    y_values = set()
    
    for point in points:
        x_values.add(point[0])
        y_values.add(point[1])
    
    if len(x_values) != 3 or len(y_values) != 3:
        return "ugly"
    
    x_sorted = sorted(x_values)
    y_sorted = sorted(y_values)
    
    if (x_sorted[1], y_sorted[1]) in points:
        return "ugly"
    
    return "respectable"

points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

print(is_respectable(points))
```
