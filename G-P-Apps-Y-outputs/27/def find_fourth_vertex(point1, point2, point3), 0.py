
def find_fourth_vertex(point1, point2, point3):
    x_values = [point1[0], point2[0], point3[0]]
    y_values = [point1[1], point2[1], point3[1]]
    
    x_values.sort()
    y_values.sort()
    
    x_count = {}
    y_count = {}
    
    for x in x_values:
        if x in x_count:
            x_count[x] += 1
        else:
            x_count[x] = 1
    
    for y in y_values:
        if y in y_count:
            y_count[y] += 1
        else:
            y_count[y] = 1
    
    x = y = None
    
    for key, value in x_count.items():
        if value == 1:
            x = key
            break
    
    for key, value in y_count.items():
        if value == 1:
            y = key
            break
    
    return x, y

point1 = (5, 5)
point2 = (5, 7)
point3 = (7, 5)

fourth_vertex = find_fourth_vertex(point1, point2, point3)
print(fourth_vertex)
```
