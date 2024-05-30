
import sys

def expected_occupancy(n, g, t, capacities):
    dp = [[0.0] * (t * g + 1) for _ in range(n + 1)]
    dp[0][0] = 1.0

    for i in range(1, n + 1):
        for j in range(t * g + 1):
            for k in range(1, min(g, j) + 1):
                dp[i][j] += dp[i - 1][j - k] / g

    expected_people = 0.0
    for i in range(1, n + 1):
        for j in range(1, t * g + 1):
            expected_people += dp[i][j] * min(j, capacities[i - 1])

    return expected_people

# Read input
n, g, t = map(int, input().split())
capacities = list(map(int, input().split()))

# Calculate and output the expected occupancy
result = expected_occupancy(n, g, t, capacities)
print("{:.9f}".format(result))
```

You can run this Python function with the given input format to calculate the expected number of people in the restaurant when it closes. Let me know if you need any more help with this problem! 
