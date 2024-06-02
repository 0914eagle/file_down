
def min_time_to_deliver(n, m, candies):
    times = [0] * n
    for i in range(n):
        for a, b in candies:
            time = abs(b - a)
            time = min(time, n - time)
            times[i] += time
    return times

# Input parsing
n, m = map(int, input().split())
candies = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and output the minimum time for each station
result = min_time_to_deliver(n, m, candies)
print(*result)
