
def find_missing_vertex(p1, p2, p3):
    x_values = {p1[0], p2[0], p3[0]}
    y_values = {p1[1], p2[1], p3[1]}
    
    x_missing = (x_values - {max(x_values), min(x_values)}).pop()
    y_missing = (y_values - {max(y_values), min(y_values)}).pop()
    
    return (x_missing, y_missing)

# Input points
p1 = (5, 5)
p2 = (5, 7)
p3 = (7, 5)

# Find the missing vertex
missing_vertex = find_missing_vertex(p1, p2, p3)

print(missing_vertex[0], missing_vertex[1])
```
