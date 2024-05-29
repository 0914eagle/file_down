
def find_maximum_subrectangle(n, m, x, y, a, b):
    center_x = (2*x+1) / 2
    center_y = (2*y+1) / 2
    
    min_distance = float('inf')
    best_rect = None
    
    for x1 in range(x + 1):
        for x2 in range(x, n + 1):
            for y1 in range(y + 1):
                for y2 in range(y, m + 1):
                    if (x2 - x1) / (y2 - y1) == a / b:
                        rect_center_x = (x1 + x2) / 2
                        rect_center_y = (y1 + y2) / 2
                        
                        distance = ((rect_center_x - center_x)**2 + (rect_center_y - center_y)**2)**0.5
                        if distance < min_distance:
                            min_distance = distance
                            best_rect = (x1, y1, x2, y2)
    
    return best_rect

# Input
n, m, x, y, a, b = map(int, input().split())

# Output
x1, y1, x2, y2 = find_maximum_subrectangle(n, m, x, y, a, b)
print(x1, y1, x2, y2)
```
