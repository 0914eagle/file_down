
def check_respectable(points):
    x_vals = set()
    y_vals = set()
    
    for x, y in points:
        x_vals.add(x)
        y_vals.add(y)
    
    if len(x_vals) != 3 or len(y_vals) != 3:
        return "ugly"
    
    x_vals.remove(sum(x_vals) // 3)
    y_vals.remove(sum(y_vals) // 3)
    
    if len(x_vals) == 1 and len(y_vals) == 1:
        return "respectable"
    else:
        return "ugly"

# Read input
points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

# Check if the points are respectable
result = check_respectable(points)
print(result)
```
