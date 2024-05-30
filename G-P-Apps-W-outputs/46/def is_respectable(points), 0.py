
def is_respectable(points):
    # Sort points based on x and y coordinates
    points.sort(key=lambda p: (p[0], p[1]))

    # Check if the set of points is respectable
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            if (points[i], points[j + 3]) not in points:
                return "ugly"
    
    return "respectable"

# Read input points
points = []
for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

# Check if points are respectable
print(is_respectable(points))
```
