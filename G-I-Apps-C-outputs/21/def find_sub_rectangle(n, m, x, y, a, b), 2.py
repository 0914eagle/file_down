
def find_sub_rectangle(n, m, x, y, a, b):
    min_distance = float('inf')
    best_rectangle = (0, 0, 0, 0)

    for x1 in range(x + 1):
        for x2 in range(x, n + 1):
            for y1 in range(y + 1):
                for y2 in range(y, m + 1):
                    if (x2 - x1) * b != (y2 - y1) * a:
                        continue

                    center_x = (x1 + x2) / 2
                    center_y = (y1 + y2) / 2
                    distance = (x - center_x) ** 2 + (y - center_y) ** 2

                    if distance < min_distance or (distance == min_distance and (x1, y1, x2, y2) < best_rectangle):
                        min_distance = distance
                        best_rectangle = (x1, y1, x2, y2)

    return best_rectangle

# Input
n, m, x, y, a, b = map(int, input().split())
# Output
x1, y1, x2, y2 = find_sub_rectangle(n, m, x, y, a, b)
print(x1, y1, x2, y2)
```
