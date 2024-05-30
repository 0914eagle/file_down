
import math

def expected_occupancy(n, g, t, capacities):
    dp = [0.0] * (t * g + 1)
    dp[0] = 1.0

    for _ in range(1, t + 1):
        new_dp = [0.0] * (t * g + 1)
        
        for i in range(t * g + 1):
            for cap in capacities:
                for k in range(1, min(g, cap) + 1):
                    if i - k >= 0:
                        new_dp[i] += dp[i - k] / g
        
        dp = new_dp

    expected_occupancy = sum(i * dp[i] for i in range(1, t * g + 1))
    return expected_occupancy

# Input parsing
n, g, t = map(int, input().split())
capacities = list(map(int, input().split()))

result = expected_occupancy(n, g, t, capacities)
print("{:.9f}".format(result))
```
