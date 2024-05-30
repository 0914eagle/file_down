
def find_crashing_line_time(n, r, p):
    # Binary search to find the minimum worst-case time
    left, right = 0, r * (n - 1)
    
    while left < right:
        mid = (left + right) // 2
        time_to_run_until_mid = (mid // p) + (mid // r) * n
        
        if time_to_run_until_mid < mid:
            right = mid
        else:
            left = mid + 1
    
    return left

# Input parsing
n, r, p = map(int, input().split())

# Find and output the worst-case time
result = find_crashing_line_time(n, r, p)
print(result)
```
