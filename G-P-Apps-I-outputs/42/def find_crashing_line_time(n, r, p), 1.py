
def find_crashing_line_time(n, r, p):
    if n == 1:
        return 0
    
    low = 0
    high = r * n
    while low < high:
        mid = (low + high) // 2
        num_printfs = mid // p
        lines_before_printf = n // 2
        
        if num_printfs >= lines_before_printf:
            high = mid
        else:
            low = mid + 1
    
    return high

# Input
n, r, p = map(int, input().split())

# Output
print(find_crashing_line_time(n, r, p))
```
