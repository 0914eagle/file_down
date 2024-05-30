
def max_longevity(n, p, c, pills):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for t, x, y in pills:
            if i >= t:
                dp[i] = max(dp[i], dp[max(0, i - t - c)] + (i - max(0, i - t - c) - c) * y // x)

    return dp[n]

# Input parsing
n, p, c = map(int, input().split())
pills = [tuple(map(int, input().split())) for _ in range(p)]

print("{:.6f}".format(max_longevity(n, p, c, pills)))
```
