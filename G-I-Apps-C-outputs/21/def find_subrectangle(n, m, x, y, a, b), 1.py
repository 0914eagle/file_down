
def find_subrectangle(n, m, x, y, a, b):
    dx = min(x, n - x)
    dy = min(y, m - y)
    
    if dx * b <= a * dy:  # maximizing width
        x1 = max(0, x - dx * a // b)
        x2 = min(n, x + dx * a // b)
        y1 = max(0, y - dx)
        y2 = min(m, y + dx)
    else:  # maximizing height
        y1 = max(0, y - dy * b // a)
        y2 = min(m, y + dy * b // a)
        x1 = max(0, x - dy)
        x2 = min(n, x + dy)
    
    return x1, y1, x2, y2

# Input
n, m, x, y, a, b = map(int, input().split())

# Output
result = find_subrectangle(n, m, x, y, a, b)
print(*result)
```
