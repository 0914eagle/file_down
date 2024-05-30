
def max_profit(n, snacks):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_profit = 0
        for j in range(1, i + 1):
            f, p, m, s = snacks[j - 1]
            if i - f >= 0:
                max_profit = max(max_profit, dp[i - f] + m * p - m * m)
        dp[i] = max(dp[i - 1], max_profit)
    return dp[n]

# Read input
n = int(input())
snacks = []
for _ in range(n):
    f, p, m, s = map(int, input().split())
    snacks.append((f, p, m, s))

# Calculate and output the maximum profit
print(max_profit(n, snacks))
```
