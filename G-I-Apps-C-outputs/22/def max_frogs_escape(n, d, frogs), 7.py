
def max_frogs_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[1], reverse=True)  # Sort frogs by weight in descending order
    dp = [0] * (n + 1)  # Initialize dynamic programming array

    for i in range(n):
        leap, weight, height = frogs[i]
        for j in range(n, 0, -1):
            if dp[j-1] + weight <= weight * 2:  # Check if the weight constraint is satisfied
                dp[j] = max(dp[j], min(dp[j-1] + leap, d) if dp[j] + height > d else dp[j])

    return dp.index(max(filter(lambda x: x <= d, dp)))  # Find the maximum number of frogs that can escape

n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

print(max_frogs_escape(n, d, frogs))
```
