
def max_longevity(n, p, c, pills):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        
        for pill_time, x, y in pills:
            if i >= pill_time:
                dp[i] = max(dp[i], dp[max(0, i - x - c)] + y)
    
    return dp[n]

# Input parsing
n, p, c = map(int, input().split())
pills = []
for _ in range(p):
    t, x, y = map(int, input().split())
    pills.append((t, x, y))

result = max_longevity(n, p, c, pills)
print("{:.6f}".format(result))
```
