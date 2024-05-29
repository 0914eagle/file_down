
def time_to_deliver(n, m, candies):
    deliver_times = [0] * n
    
    for i in range(n):
        time = 0
        for a, b in candies:
            dist = abs(a - b)
            time += min(dist, n - dist) + 1
        deliver_times[i] = time
    
    return deliver_times

# Input
n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(m)]

# Output
result = time_to_deliver(n, m, candies)
print(*result)
```
