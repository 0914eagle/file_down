
def max_life(n, p, c, pills):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i-1] + 1
        for t, x, y in pills:
            if i >= t:
                dp[i] = max(dp[i], dp[i-x] + y)
        if i > 0:
            dp[i] = max(dp[i], dp[i-1] - c)
    return dp[n]

# Input parsing
n, p, c = map(int, input().split())
pills = []
for _ in range(p):
    t, x, y = map(int, input().split())
    pills.append((t, x, y))

result = max_life(n, p, c, pills)
print("{:.6f}".format(result))
```
