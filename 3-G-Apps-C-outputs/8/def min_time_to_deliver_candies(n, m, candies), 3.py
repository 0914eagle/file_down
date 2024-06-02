
def min_time_to_deliver_candies(n, m, candies):
    times = [0] * n
    for i in range(n):
        for a, b in candies:
            time = abs(i - a) + 1
            time += abs(a - b) if a <= b else n - a + b
            times[i] = max(times[i], time)
    return times

# Input parsing
n, m = map(int, input().split())
candies = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and print the minimum time for each station
result = min_time_to_deliver_candies(n, m, candies)
print(*result)
