
def check_respectable(points):
    x_values = []
    y_values = []
    
    for point in points:
        x_values.append(point[0])
        y_values.append(point[1])
    
    x_values.sort()
    y_values.sort()
    
    x_avg = sum(x_values) // 8
    y_avg = sum(y_values) // 8
    
    x_values.remove(x_avg)
    y_values.remove(y_avg)
    
    if len(set(x_values)) == 3 and len(set(y_values)) == 3:
        return "respectable"
    else:
        return "ugly"

# Input
points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

# Output
print(check_respectable(points))
```
