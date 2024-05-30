
def max_life(n, p, c, pills):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = dp[i-1] + 1
        for t, x, y in pills:
            if i >= t:
                dp[i] = max(dp[i], dp[i-(t+c)] + (t-c-y)*x)
    
    return dp[n]

# Read input
n, p, c = map(int, input().split())
pills = [list(map(int, input().split())) for _ in range(p)]

# Calculate and output the result
result = max_life(n, p, c, pills)
print(f"{result:.6f}")
```
