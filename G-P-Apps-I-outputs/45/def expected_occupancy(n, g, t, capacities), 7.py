
import sys

def expected_occupancy(n, g, t, capacities):
    dp = [[[0.0 for _ in range(n * g + 1)] for _ in range(n)] for _ in range(t + 1)]
    dp[0][0][0] = 1.0

    for hour in range(1, t + 1):
        for table in range(n):
            for people in range(n * g + 1):
                for group_size in range(1, g + 1):
                    if people >= group_size:
                        dp[hour][table][people] += dp[hour - 1][table][people - group_size] / g
                    else:
                        dp[hour][table][people] += dp[hour - 1][table][people] / g

                    if table > 0:
                        dp[hour][table][people] += dp[hour - 1][table - 1][people] / g

    expected_sum = 0.0
    for table in range(n):
        for people in range(n * g + 1):
            expected_sum += dp[t][table][people] * people

    return expected_sum

# Read input
n, g, t = map(int, input().split())
capacities = list(map(int, input().split()))

# Calculate and output expected occupancy
result = expected_occupancy(n, g, t, capacities)
print("{:.9f}".format(result))
```
