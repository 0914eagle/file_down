
h, w = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
MOD = 10**9 + 7
dp = [[0]*(w+1) for _ in range(h+1)]
dp[0][0] = 1
for i in range(1, h+1):
    for j in range(1, w+1):
        dp[i][j] = dp[i][j-1]
        if r[i-1] > 0:
            if j-r[i-1] >= 0:
                dp[i][j] += dp[i-1][j-r[i-1]]
        dp[i][j] %= MOD
ans = 0
for j in range(1, w+1):
    if c[j-1] > 0:
        if j-c[j-1] >= 0:
            ans += dp[h][j-c[j-1]]
print(ans % MOD)

