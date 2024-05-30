
import math

def expected_occupancy(n, g, t, capacities):
    total_capacity = sum(capacities)
    dp = [[[0 for _ in range(total_capacity + 1)] for _ in range(t)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, t):
            for k in range(total_capacity + 1):
                for x in range(1, min(g, k) + 1):
                    dp[i][j][k] += dp[i - 1][j - 1][k - x] / g

    expected_occupancy = 0
    for i in range(1, n + 1):
        for k in range(1, total_capacity + 1):
            expected_occupancy += i * dp[i][t - 1][k]

    return expected_occupancy

# Input processing
n, g, t = map(int, input().split())
capacities = list(map(int, input().split()))

result = expected_occupancy(n, g, t, capacities)
print("{:.9f}".format(result))
```
