
def min_time_to_deliver(n, m, candies):
    stations = [0] * n
    for i in range(n):
        for a, b in candies:
            dist = min(abs(a - i - 1), n - abs(a - i - 1)) + abs(a - b - 1)
            stations[i] = max(stations[i], dist)
    return stations

# Input parsing
n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print the minimum time for each station
result = min_time_to_deliver(n, m, candies)
print(*result)
