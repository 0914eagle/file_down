
import sys

# Read inputs
n, g, t = map(int, input().split())
capacities = list(map(int, input().split()))

# Initialize dp array to store expected numbers of people after each hour
dp = [[0.0 for _ in range(sum(capacities) * t + 1)] for _ in range(t + 1)]

# Initialize base case
dp[0][0] = 1.0

# Fill dp array
for hour in range(1, t + 1):
    for occupied in range(sum(capacities) * (hour - 1) + 1):
        for c in capacities:
            for group in range(1, g + 1):
                dp[hour][occupied + min(group, c)] += dp[hour - 1][occupied] / g

# Calculate expected occupancy after t hours
expected_sum = 0.0
for hour in range(1, t + 1):
    for occupied in range(sum(capacities) * t + 1):
        expected_sum += dp[hour][occupied] * occupied

print("%.9f" % expected_sum)
```
