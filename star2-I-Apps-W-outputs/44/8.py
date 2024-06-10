
n, m, k = map(int, input().split())
mod = 998244353
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, m+1):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(1, m+1):
        dp[i][j] = sum(dp[i-1]) % mod
        if i-1 >= k+1:
            dp[i][j] = (dp[i][j] - dp[i-1][j] + mod) % mod
print(sum(dp[n]) % mod)

