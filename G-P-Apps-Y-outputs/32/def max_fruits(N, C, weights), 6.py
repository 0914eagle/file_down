
def max_fruits(N, C, weights):
    dp = [0] * (C + 1)
    for w in weights:
        for c in range(C, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + 1)
    return dp[C]

# Read input
N, C = map(int, input().split())
weights = list(map(int, input().split()))

# Call the function
result = max_fruits(N, C, weights)
print(result)
```
