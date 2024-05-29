
def max_frogs_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[2], reverse=True)

    ans = 0
    dp = [0] * (d + 1)
    for i in range(n):
        leap, weight, height = frogs[i]
        for j in range(d, height - leap, -1):
            if dp[j - height] + weight <= dp[j]:
                dp[j] = dp[j - height] + weight
                ans = max(ans, dp[j])

    return ans

# Read input
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

# Calculate and output the maximum number of frogs that can escape the pit
print(max_frogs_escape(n, d, frogs))
```
