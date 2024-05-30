
def max_profit(n, snacks):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        f, p, m, s = snacks[i - 1]
        dp[i] = max(dp[i - 1], dp[f] + (m - p) * s)
    
    return dp[n]

# Read input
n = int(input())
snacks = []
for _ in range(n):
    f, p, m, s = map(int, input().split())
    snacks.append((f, p, m, s))

# Calculate and print the maximum profit
print(max_profit(n, snacks))
```
