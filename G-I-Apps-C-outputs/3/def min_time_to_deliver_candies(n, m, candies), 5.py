
def min_time_to_deliver_candies(n, m, candies):
    time_needed = [0] * n
    for start_station in range(1, n+1):
        for candy in candies:
            ai, bi = candy
            time = 0
            if ai <= start_station:
                time = max(start_station, bi) - ai
            else:
                time = n - ai + bi + n - start_station
            time_needed[start_station - 1] += time
    return time_needed

n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(m)]

result = min_time_to_deliver_candies(n, m, candies)
print(*result)
```
