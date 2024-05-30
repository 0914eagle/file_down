
def find_fourth_point(p1, p2, p3):
    x_values = [p1[0], p2[0], p3[0]]
    y_values = [p1[1], p2[1], p3[1]]
    
    x_values.sort()
    y_values.sort()
    
    x_fourth = x_values[0] if x_values.count(x_values[0]) == 1 else x_values[2]
    y_fourth = y_values[0] if y_values.count(y_values[0]) == 1 else y_values[2]
    
    return (x_fourth, y_fourth)

# Input
p1 = (5, 5)
p2 = (5, 7)
p3 = (7, 5)

# Output
fourth_point = find_fourth_point(p1, p2, p3)
print(fourth_point[0], fourth_point[1])
```
