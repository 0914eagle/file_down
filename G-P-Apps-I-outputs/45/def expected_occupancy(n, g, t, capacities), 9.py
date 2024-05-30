
import sys

def expected_occupancy(n, g, t, capacities):
    dp = [[[0.0 for _ in range(g+1)] for _ in range(sum(capacities)+1)] for _ in range(t+1)]
    dp[0][0][0] = 1.0

    for hour in range(1, t+1):
        for people in range(sum(capacities)+1):
            for group_size in range(1, g+1):
                for table_capacity in capacities:
                    for occupied in range(table_capacity, people+1):
                        dp[hour][people][group_size] += dp[hour-1][people - occupied][group_size-1] / table_capacity

    expected_occupancy = 0.0
    for people in range(sum(capacities)+1):
        for group_size in range(1, g+1):
            expected_occupancy += people * dp[t][people][group_size]

    return expected_occupancy

# Read input
n, g, t = map(int, input().split())
capacities = list(map(int, input().split()))

# Calculate and output result
result = expected_occupancy(n, g, t, capacities)
print("{:.9f}".format(result))
```
