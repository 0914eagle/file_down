
def find_missing_vertex(point1, point2, point3):
    x_values = [point1[0], point2[0], point3[0]]
    y_values = [point1[1], point2[1], point3[1]]
    
    x_set = set(x_values)
    y_set = set(y_values)
    
    for x in x_set:
        if x_values.count(x) == 1:
            missing_x = x
    for y in y_set:
        if y_values.count(y) == 1:
            missing_y = y
    
    return missing_x, missing_y

# Input points
point1 = (5, 5)
point2 = (5, 7)
point3 = (7, 5)

missing_vertex = find_missing_vertex(point1, point2, point3)
print(missing_vertex[0], missing_vertex[1])
```
