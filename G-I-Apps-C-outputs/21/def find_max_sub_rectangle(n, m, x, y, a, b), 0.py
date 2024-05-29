
def find_max_sub_rectangle(n, m, x, y, a, b):
    min_dist = float('inf')
    min_dist_rect = None
    
    for x1 in range(x+1):
        for y1 in range(y+1):
            for x2 in range(x, n+1):
                for y2 in range(y, m+1):
                    if (x2 - x1) * b == (y2 - y1) * a:
                        rect_center_x = (x1 + x2) / 2
                        rect_center_y = (y1 + y2) / 2
                        dist = ((x - rect_center_x) ** 2 + (y - rect_center_y) ** 2) ** 0.5
                        
                        if dist < min_dist or (dist == min_dist and (x1, y1, x2, y2) < min_dist_rect):
                            min_dist = dist
                            min_dist_rect = (x1, y1, x2, y2)
    
    return min_dist_rect

# Input
n, m, x, y, a, b = map(int, input().split())
# Output
result = find_max_sub_rectangle(n, m, x, y, a, b)
print(*result)
```
