
import sys

def expected_occupancy(n, g, t, capacities):
    dp = [[[0.0 for _ in range(n * g + 1)] for _ in range(n + 1)] for _ in range(t + 1)]
    dp[0][0][0] = 1.0

    for i in range(1, t + 1):
        for j in range(1, n + 1):
            for k in range(1, n * g + 1):
                for l in range(1, min(k, g) + 1):
                    dp[i][j][k] += dp[i - 1][j - 1][k - l] / n

    expected_occupancy = 0.0
    for i in range(1, n + 1):
        for j in range(1, n * g + 1):
            expected_occupancy += i * dp[t][i][j]

    return expected_occupancy

# Read input
n, g, t = map(int, input().split())
capacities = list(map(int, input().split()))

# Calculate and output the expected occupancy
result = expected_occupancy(n, g, t, capacities)
print("{:.9f}".format(result))
```
