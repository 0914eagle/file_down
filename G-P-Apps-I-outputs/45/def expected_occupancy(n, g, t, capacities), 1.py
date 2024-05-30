
def expected_occupancy(n, g, t, capacities):
    total_capacity = sum(capacities)
    dp = [[0.0] * (total_capacity + 1) for _ in range(t + 1)]
    dp[0][0] = 1.0

    for hour in range(1, t + 1):
        for people in range(total_capacity + 1):
            for cap in capacities:
                for size in range(1, min(g, cap) + 1):
                    new_people = min(people + size, total_capacity)
                    dp[hour][new_people] += dp[hour - 1][people] / min(g, cap)

    expected_occupancy = sum(i * dp[t][i] for i in range(total_capacity + 1))
    return expected_occupancy

# Input
n, g, t = map(int, input().split())
capacities = list(map(int, input().split()))

# Output
result = expected_occupancy(n, g, t, capacities)
print("{:.9f}".format(result))
```
