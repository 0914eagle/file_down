
def max_profit(n, snacks):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + snacks[i - 1][2] - snacks[j][1] if snacks[j][0] == i else 0)
    
    return max(dp)

# Read input
n = int(input())
snacks = []
for _ in range(n):
    f, p, m, s = map(int, input().split())
    snacks.append((f, p, m, s))

# Calculate and print maximum profit
print(max_profit(n, snacks))
```
