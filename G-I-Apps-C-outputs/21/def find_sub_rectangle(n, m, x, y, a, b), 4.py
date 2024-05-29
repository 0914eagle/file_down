
def find_sub_rectangle(n, m, x, y, a, b):
    low = 0
    high = min(n // a, m // b)
    closest_dist = float('inf')
    result = (0, 0, 0, 0)
    
    for i in range(1, high + 1):
        j = i * b // a
        x1 = max(0, x - i)
        y1 = max(0, y - j)
        x2 = min(n, x + i)
        y2 = min(m, y + j)
        
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        
        dist = ((center_x - x) ** 2 + (center_y - y) ** 2) ** 0.5
        
        if dist < closest_dist or (dist == closest_dist and (x1, y1, x2, y2) < result):
            closest_dist = dist
            result = (x1, y1, x2, y2)
    
    return result

# Input
n, m, x, y, a, b = map(int, input().split())

# Output
x1, y1, x2, y2 = find_sub_rectangle(n, m, x, y, a, b)
print(x1, y1, x2, y2)
```
