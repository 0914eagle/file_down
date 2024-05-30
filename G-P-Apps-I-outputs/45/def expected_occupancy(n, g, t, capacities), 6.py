
import sys

def expected_occupancy(n, g, t, capacities):
    dp = [0.0] * (t * g + 1)
    dp[0] = 1.0

    for cap in capacities:
        new_dp = [0.0] * (t * g + 1)

        for i in range(len(dp)):
            for j in range(1, min(g, cap) + 1):
                new_dp[min(i + j, t * g)] += dp[i] / g

        dp = new_dp

    expected_people = sum(i * dp[i] for i in range(len(dp)))
    return expected_people

# Read input
n, g, t = map(int, input().split())
capacities = list(map(int, input().split()))

# Calculate and output the expected occupancy
result = expected_occupancy(n, g, t, capacities)
print("{:.9f}".format(result))
```
