
def check_respectable(points):
    # Extract x and y coordinates
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    
    # Sort coordinates
    x_coords.sort()
    y_coords.sort()
    
    # Calculate average point
    avg_x = sum(x_coords) // 8
    avg_y = sum(y_coords) // 8
    avg_point = (avg_x, avg_y)
    
    # Check if average point is in the set
    if avg_point in points:
        return "ugly"
    
    # Check if the set contains all points except the average
    for i in range(3):
        for j in range(3):
            if (x_coords[i], y_coords[j]) not in points:
                return "ugly"
    
    return "respectable"

# Input
points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

# Output
print(check_respectable(points))
```
