
def find_fourth_point(p1, p2, p3):
    x_coords = [p1[0], p2[0], p3[0]]
    y_coords = [p1[1], p2[1], p3[1]]

    x_set = set(x_coords)
    y_set = set(y_coords)

    fourth_x = (x_set.pop() if x_coords.count(x_set.pop()) == 1 else x_set.pop())
    fourth_y = (y_set.pop() if y_coords.count(y_set.pop()) == 1 else y_set.pop())

    return (fourth_x, fourth_y)

# Read the three points
points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

# Find the fourth point
fourth_point = find_fourth_point(points[0], points[1], points[2])

# Output the coordinates of the fourth point
print(*fourth_point)
```
