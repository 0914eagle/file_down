
def max_profit(n, snacks):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], dp[j])
            if snacks[j][0] == i:
                dp[i] = max(dp[i], dp[j] + snacks[i-1][2] - snacks[j][1] * snacks[i-1][3])
    return dp[n]

# Reading input
n = int(input())
snacks = []
for _ in range(n):
    f, p, m, s = map(int, input().split())
    snacks.append((f, p, m, s))

# Calculating and printing the maximum profit
print(max_profit(n, snacks))
```
