
MOD = 998244353

n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [[0] * (k + 1) for i in range(n)]
dp[0][h[0]] = 1

for i in range(1, n):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j]
    for j in range(1, k + 1):
        dp[i][j] += dp[i - 1][j - 1]
        dp[i][j] %= MOD

ans = 0
for i in range(1, k + 1):
    ans += dp[n - 1][i]
    ans %= MOD

print(ans)

