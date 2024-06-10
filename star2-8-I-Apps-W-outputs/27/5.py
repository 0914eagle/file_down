
h, w = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
MOD = 10**9 + 7
dp = [[0 for _ in range(w+1)] for _ in range(h+1)]
dp[0][0] = 1
for i in range(1, h+1):
    for j in range(1, w+1):
        if r[i-1] > 0 and c[j-1] > 0:
            dp[i][j] = dp[i-1][j] * r[i-1] + dp[i][j-1] * c[j-1]
            dp[i][j] %= MOD
            r[i-1] -= 1
            c[j-1] -= 1
        elif r[i-1] > 0:
            dp[i][j] = dp[i-1][j] * r[i-1]
            r[i-1] -= 1
        elif c[j-1] > 0:
            dp[i][j] = dp[i][j-1] * c[j-1]
            c[j-1] -= 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= MOD
print(dp[h][w])

