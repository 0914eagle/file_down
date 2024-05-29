
def min_time_to_deliver_all_candies(n, m, candies):
    times = [0] * n
    for i in range(n):
        for ai, bi in candies:
            time = min(abs(i - ai), n - abs(i - ai)) + abs(ai - bi)
            times[i] = max(times[i], time)
    return times

# Input processing
n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(m)]

# Get the minimum time needed for the train to deliver all candies from each starting station
results = min_time_to_deliver_all_candies(n, m, candies)

# Output the results
print(*results)
