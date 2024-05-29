
def find_subrectangle(n, m, x, y, a, b):
    x1 = max(0, x - int((a * (y+b) - b*x) / b))
    y1 = max(0, y - int((b * (x+a) - a*y) / a))
    x2 = min(n, x + int((a * (m-y) - b*(m-y)) / b))
    y2 = min(m, y + int((b * (n-x) - a*(n-x)) / a))
    
    return x1, y1, x2, y2

n, m, x, y, a, b = map(int, input().split())
x1, y1, x2, y2 = find_subrectangle(n, m, x, y, a, b)
print(x1, y1, x2, y2)
```
