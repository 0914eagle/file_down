
def find_sub_rectangle(n, m, x, y, a, b):
    x_center = x
    y_center = y
    if x < n / 2:
        if y < m / 2:
            x1 = max(0, x - int(a * min(x, b / 2) / b))
            y1 = max(0, y - int(b * min(y, a / 2) / a))
            x2 = min(n, x + int(a * min(n - x, b / 2) / b))
            y2 = min(m, y + int(b * min(m - y, a / 2) / a))
        else:
            x1 = max(0, x - int(a * min(x, b / 2) / b))
            y1 = max(0, y - int(b * min(m - y, a / 2) / a))
            x2 = min(n, x + int(a * min(n - x, b / 2) / b))
            y2 = min(m, y + int(b * min(y, a / 2) / a))
    else:
        if y < m / 2:
            x1 = max(0, x - int(a * min(n - x, b / 2) / b))
            y1 = max(0, y - int(b * min(y, a / 2) / a))
            x2 = min(n, x + int(a * min(x, b / 2) / b))
            y2 = min(m, y + int(b * min(m - y, a / 2) / a))
        else:
            x1 = max(0, x - int(a * min(n - x, b / 2) / b))
            y1 = max(0, y - int(b * min(m - y, a / 2) / a))
            x2 = min(n, x + int(a * min(x, b / 2) / b))
            y2 = min(m, y + int(b * min(y, a / 2) / a))
    
    return x1, y1, x2, y2

# Input
n, m, x, y, a, b = map(int, input().split())

# Output
x1, y1, x2, y2 = find_sub_rectangle(n, m, x, y, a, b)
print(x1, y1, x2, y2)
```
