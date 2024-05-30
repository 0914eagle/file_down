
def find_fourth_point(p1, p2, p3):
    x_coords = [p1[0], p2[0], p3[0]]
    y_coords = [p1[1], p2[1], p3[1]]
    
    fourth_x = min(x_coords) + max(x_coords) - min(x_coords)
    fourth_y = min(y_coords) + max(y_coords) - min(y_coords)
    
    return (fourth_x, fourth_y)

# Input
p1 = tuple(map(int, input().split()))
p2 = tuple(map(int, input().split()))
p3 = tuple(map(int, input().split()))

# Output
fourth_point = find_fourth_point(p1, p2, p3)
print(fourth_point[0], fourth_point[1])
```
