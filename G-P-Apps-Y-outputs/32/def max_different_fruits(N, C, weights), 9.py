
def max_different_fruits(N, C, weights):
    dp = [0] * (C + 1)
    for w in weights:
        for i in range(C, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + 1)
    return dp[C]

# Read input
N, C = map(int, input().split())
weights = list(map(int, input().split()))

# Call the function and output the result
result = max_different_fruits(N, C, weights)
print(result)
```
