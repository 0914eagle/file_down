
def max_fruits(N, C, weights):
    dp = [0] * (C + 1)
    for w in weights:
        for i in range(C, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + 1)
    return dp[C]

# Reading input
N, C = map(int, input().split())
weights = list(map(int, input().split()))

# Calling the function and printing the result
print(max_fruits(N, C, weights))
```
