
def calculate_delivery_times(n, m, candies):
    delivery_times = [0] * n
    
    for i in range(n):
        for candy in candies:
            start_station = i + 1
            end_station = candy[1]

            time_to_pickup = abs(start_station - candy[0])
            time_to_deliver = abs(end_station - candy[1])
            
            time_taken = min(time_to_pickup, n - time_to_pickup) + 1 + time_to_deliver
            delivery_times[i] = max(delivery_times[i], time_taken)

    return delivery_times


# Input reading
n, m = map(int, input().split())
candies = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and print delivery times
result = calculate_delivery_times(n, m, candies)
print(*result)
```
