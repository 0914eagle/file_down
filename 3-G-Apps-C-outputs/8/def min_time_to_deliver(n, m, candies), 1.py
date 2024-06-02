
def min_time_to_deliver(n, m, candies):
    times = [0] * n
    for i in range(n):
        for a, b in candies:
            dist = abs(b - a)
            time = min(dist, n - dist) + 1
            times[i] += time
    return times

# Input
n, m = map(int, input().split())
candies = [tuple(map(int, input().split())) for _ in range(m)]

# Output
result = min_time_to_deliver(n, m, candies)
print(*result)
