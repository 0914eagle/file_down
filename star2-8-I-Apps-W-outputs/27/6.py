
h, w = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[0][0] = 1
mod = 10**9 + 7
for i in range(1, h + 1):
    for j in range(1, w + 1):
        dp[i][j] = dp[i - 1][j] * (c[j - 1] + 1) % mod
        dp[i][j] += dp[i][j - 1] * (r[i - 1] + 1) % mod
        dp[i][j] %= mod
print(dp[h][w])

