
def find_subrectangle(n, m, x, y, a, b):
    center_x = x + 0.5
    center_y = y + 0.5
    
    ratio = a / b
    min_dist = float('inf')
    res_x1, res_y1, res_x2, res_y2 = 0, 0, 0, 0
    
    for x1 in range(x + 1):
        for y1 in range(y + 1):
            for x2 in range(x, n + 1):
                for y2 in range(y, m + 1):
                    if (x2 - x1) / (y2 - y1) == ratio:
                        cx = (x1 + x2) / 2
                        cy = (y1 + y2) / 2
                        dist = (cx - center_x) ** 2 + (cy - center_y) ** 2
                        if dist < min_dist or (dist == min_dist and (x1, y1, x2, y2) < (res_x1, res_y1, res_x2, res_y2)):
                            min_dist = dist
                            res_x1, res_y1, res_x2, res_y2 = x1, y1, x2, y2
    
    return res_x1, res_y1, res_x2, res_y2

# Input
n, m, x, y, a, b = map(int, input().split())

# Output
result = find_subrectangle(n, m, x, y, a, b)
print(' '.join(map(str, result)))
```
