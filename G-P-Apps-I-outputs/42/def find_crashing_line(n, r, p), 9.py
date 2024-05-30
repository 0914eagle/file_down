
def find_crashing_line(n, r, p):
    if n == 1:
        return 0
    
    left = 0
    right = n - 1
    time = 0
    
    while left < right:
        mid = (left + right) // 2
        time += p
        if mid >= r / 2:
            right = mid
        else:
            left = mid + 1
    
    return time

# Input
n, r, p = map(int, input().split())

# Output
print(find_crashing_line(n, r, p))
```
