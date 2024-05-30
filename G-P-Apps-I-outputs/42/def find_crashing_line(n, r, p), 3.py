
def find_crashing_line(n, r, p):
    min_time = 0
    max_time = r
    
    while min_time < max_time:
        mid = (min_time + max_time) // 2
        lines_before_mid = mid // p
        lines_after_mid = n - lines_before_mid
        
        time_before_mid = lines_before_mid * p
        time_after_mid = lines_after_mid * p
        
        total_time = max(time_before_mid, time_after_mid)
        
        if total_time >= mid:
            max_time = mid
        else:
            min_time = mid + 1
    
    return min_time

# Input
n, r, p = map(int, input().split())

# Output
print(find_crashing_line(n, r, p))
```
