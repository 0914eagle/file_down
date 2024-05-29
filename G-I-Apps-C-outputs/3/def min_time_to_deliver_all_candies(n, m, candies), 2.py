
def min_time_to_deliver_all_candies(n, m, candies):
    time_needed = []
    
    for start_station in range(1, n+1):
        time = 0
        for i in range(m):
            from_station, to_station = candies[i]
            time += min(abs(from_station - start_station), n - abs(from_station - start_station)) + min(abs(to_station - from_station), n - abs(to_station - from_station))
        time_needed.append(time)
    
    return time_needed

# Input parsing
n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print the result
result = min_time_to_deliver_all_candies(n, m, candies)
print(' '.join(map(str, result)))
```
