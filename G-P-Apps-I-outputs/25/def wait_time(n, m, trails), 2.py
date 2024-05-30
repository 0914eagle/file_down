
def wait_time(n, m, trails):
    cabin_times = [float('inf')] * n
    cabin_times[0] = 0
    
    for _ in range(n-1):
        for u, v, d in trails:
            cabin_times[v] = min(cabin_times[v], cabin_times[u] + d)
    
    return max(0, cabin_times[n-1] - 12)

# Input parsing
n, m = map(int, input().split())
trails = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and output the wait time
result = wait_time(n, m, trails)
print(result)
```
