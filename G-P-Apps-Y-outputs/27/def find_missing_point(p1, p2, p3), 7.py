
def find_missing_point(p1, p2, p3):
    x_values = [p1[0], p2[0], p3[0]]
    y_values = [p1[1], p2[1], p3[1]]
    
    x_counts = {}
    y_counts = {}
    
    for x in x_values:
        x_counts[x] = x_counts.get(x, 0) + 1
    for y in y_values:
        y_counts[y] = y_counts.get(y, 0) + 1
        
    for x in x_counts:
        if x_counts[x] == 1:
            missing_x = x
            break
    
    for y in y_counts:
        if y_counts[y] == 1:
            missing_y = y
            break
            
    return (missing_x, missing_y)

# Sample Input
p1 = (5, 5)
p2 = (5, 7)
p3 = (7, 5)

missing_point = find_missing_point(p1, p2, p3)
print(missing_point[0], missing_point[1])
```
