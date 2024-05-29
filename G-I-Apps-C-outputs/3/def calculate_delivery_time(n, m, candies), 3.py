
def calculate_delivery_time(n, m, candies):
    delivery_times = [0] * n
    
    for i in range(n):
        time = 0
        for j in range(m):
            a, b = candies[j]
            dist = abs(a - i - 1)
            dist = min(dist, n - dist)
            time += min(dist, abs(b - a) + abs(b - i - 1))
        
        delivery_times[i] = time
    
    return delivery_times

# Input
n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(m)]

# Output
result = calculate_delivery_time(n, m, candies)
print(*result)
```
