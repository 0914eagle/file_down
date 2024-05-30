
def max_fruits(N, C, weights):
    dp = [0] * (C + 1)
    for weight in weights:
        for i in range(C, weight - 1, -1):
            dp[i] = max(dp[i], dp[i - weight] + 1)
    return dp[C]

# Read input
N, C = map(int, input().split())
weights = list(map(int, input().split()))

# Call the function
result = max_fruits(N, C, weights)

print(result)
```
