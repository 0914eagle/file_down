
def find_max_subrectangle(n, m, x, y, a, b):
    min_dist = float('inf')
    closest_rect = None

    for x1 in range(x + 1):
        for y1 in range(y + 1):
            for x2 in range(x, n + 1):
                for y2 in range(y, m + 1):
                    if (x2 - x1) * b == (y2 - y1) * a:
                        center_x = (x1 + x2) / 2
                        center_y = (y1 + y2) / 2
                        distance = (x - center_x) ** 2 + (y - center_y) ** 2
                        if distance < min_dist or (distance == min_dist and (x1, y1, x2, y2) < closest_rect):
                            min_dist = distance
                            closest_rect = (x1, y1, x2, y2)

    return closest_rect

# Input parsing
n, m, x, y, a, b = map(int, input().split())

x1, y1, x2, y2 = find_max_subrectangle(n, m, x, y, a, b)
print(x1, y1, x2, y2)
```
