
def max_lifespan(n, p, c, pills):
    dp = [0.0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1.0
        
        for j in range(p):
            t, x, y = pills[j]
            if i >= t:
                dp[i] = max(dp[i], dp[max(0, i - x)] + y, dp[t - c] + (i - t))
    
    return dp[n]

# Input parsing
n, p, c = map(int, input().split())
pills = []
for _ in range(p):
    ti, xi, yi = map(int, input().split())
    pills.append((ti, xi, yi))

result = max_lifespan(n, p, c, pills)
print('{:.9f}'.format(result))
```
