
def min_time_to_deliver(n, m, candies):
    times = [0] * n
    for station in range(1, n+1):
        for i in range(m):
            a, b = candies[i]
            time = abs(station - a)
            time = min(time, n - time)
            time += abs(a - b)  # time to deliver candy i
            if time > times[station-1]:
                times[station-1] = time
    return times

# Input
n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(m)]

# Output
result = min_time_to_deliver(n, m, candies)
print(*result)
```
