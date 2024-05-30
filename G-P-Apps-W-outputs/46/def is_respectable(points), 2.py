
def is_respectable(points):
    x_coords = set()
    y_coords = set()
    
    for x, y in points:
        x_coords.add(x)
        y_coords.add(y)
    
    if len(x_coords) != 3 or len(y_coords) != 3:
        return "ugly"
    
    x_1, x_2, x_3 = sorted(x_coords)
    y_1, y_2, y_3 = sorted(y_coords)
    
    if (x_2, y_2) in points:
        return "ugly"
    else:
        return "respectable"

points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

print(is_respectable(points))
```
