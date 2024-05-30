
def max_life(n, p, c, pills):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(p):
            t, x, y = pills[j]
            if i >= t:
                prev_time = max(0, i - t - c)
                prev_life = dp[prev_time]
                curr_life = dp[max(0, i - x)]
                dp[i] = max(dp[i], prev_life + y - curr_life)
    
    return dp[n]

# Input processing
n, p, c = map(int, input().split())
pills = []
for _ in range(p):
    t, x, y = map(int, input().split())
    pills.append((t, x, y))

# Calculate and print the maximum number of seconds you could live
print("{:.6f}".format(max_life(n, p, c, pills)))
```
