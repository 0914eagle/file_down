
def check_set(points):
    x_vals = set()
    y_vals = set()
    
    for x, y in points:
        x_vals.add(x)
        y_vals.add(y)
    
    if len(x_vals) != 3 or len(y_vals) != 3:
        return "ugly"
    
    x_vals = sorted(x_vals)
    y_vals = sorted(y_vals)
    
    avg_point = (x_vals[1], y_vals[1])
    
    points_set = set(points)
    
    for i in range(3):
        for j in range(3):
            if (x_vals[i], y_vals[j]) == avg_point:
                continue
            if (x_vals[i], y_vals[j]) not in points_set:
                return "ugly"
    
    return "respectable"

# Input
points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

# Output
print(check_set(points))
```
