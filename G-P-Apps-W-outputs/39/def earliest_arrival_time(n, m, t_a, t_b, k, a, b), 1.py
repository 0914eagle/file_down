
def earliest_arrival_time(n, m, t_a, t_b, k, a, b):
    if k >= n + m:
        return -1
    
    min_cancel = max(0, k - m)
    max_cancel = min(k, n)
    
    ans = float('inf')
    
    for i in range(min_cancel, max_cancel + 1):
        earliest = max(a[i], b[i + m - k])
        ans = min(ans, earliest + t_a + t_b)
    
    return ans

# Input reading
n, m, t_a, t_b, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Call the function and print the result
result = earliest_arrival_time(n, m, t_a, t_b, k, a, b)
print(result)
```
