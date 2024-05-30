
import sys

def expected_occupancy(n, g, t, capacities):
    dp = [[0.0] * (sum(capacities) + 1) for _ in range(t + 1)]
    dp[0][0] = 1.0

    for i in range(1, t + 1):
        for j in range(sum(capacities) + 1):
            for cap in capacities:
                for k in range(1, min(g, cap) + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k] / g

    expected_occupancy = sum(j * dp[t][j] for j in range(sum(capacities) + 1))
    return expected_occupancy

# Read input
n, g, t = map(int, input().split())
capacities = list(map(int, input().split()))

# Calculate expected occupancy
result = expected_occupancy(n, g, t, capacities)

# Print the result with 9 decimal places
print("{:.9f}".format(result))
```
