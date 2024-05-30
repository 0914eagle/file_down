
def is_respectable(points):
    x_vals = set()
    y_vals = set()
    
    for x, y in points:
        x_vals.add(x)
        y_vals.add(y)
    
    if len(x_vals) != 3 or len(y_vals) != 3:
        return "ugly"
    
    x_sorted = sorted(list(x_vals))
    y_sorted = sorted(list(y_vals))
    
    x_avg = (x_sorted[0] + x_sorted[1] + x_sorted[2]) / 3
    y_avg = (y_sorted[0] + y_sorted[1] + y_sorted[2]) / 3
    
    if (x_avg, y_avg) in points:
        return "ugly"
    else:
        return "respectable"

points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

print(is_respectable(points))
```
