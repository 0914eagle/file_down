
n, l = map(int, input().split())
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(i+1, n+1):
        dp[i+1][j] = dp[i][j] + (l + i)
ans = float('inf')
for i in range(1, n+1):
    ans = min(ans, abs(dp[i-1][n] - dp[i][n]))
print(dp[n][n] - ans)

