
def find_max_subrectangle(n, m, x, y, a, b):
    x_center = (x*a + x) // (a+1)
    y_center = (y*b + y) // (b+1)
    
    x1 = max(0, x_center - (x//a) * a)
    y1 = max(0, y_center - (y//b) * b)
    x2 = min(n, x_center + ((n-x)//a) * a)
    y2 = min(m, y_center + ((m-y)//b) * b)
    
    return x1, y1, x2, y2

# Input parsing
n, m, x, y, a, b = map(int, input().split())

# Call the function and output the result
x1, y1, x2, y2 = find_max_subrectangle(n, m, x, y, a, b)
print(x1, y1, x2, y2)
```
