
def find_fourth_vertex(p1, p2, p3):
    x_values = [p1[0], p2[0], p3[0]]
    y_values = [p1[1], p2[1], p3[1]]

    # Find the missing x and y coordinates
    x4 = max(x_values) if x_values.count(max(x_values)) == 1 else min(x_values)
    y4 = max(y_values) if y_values.count(max(y_values)) == 1 else min(y_values)

    return x4, y4

# Input points
p1 = (5, 5)
p2 = (5, 7)
p3 = (7, 5)

# Find the fourth vertex
x4, y4 = find_fourth_vertex(p1, p2, p3)

print(x4, y4)
```
