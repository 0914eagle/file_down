
n, m, k = map(int, input().split())
mod = 998244353
dp = [[0 for _ in range(m)] for _ in range(n+1)]
for i in range(m):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(m):
        for k in range(m):
            if j != k:
                dp[i][j] += dp[i-1][k]
                dp[i][j] %= mod
print(sum(dp[n]) % mod)

