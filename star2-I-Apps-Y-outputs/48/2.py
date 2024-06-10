
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * (m + 1) for i in range(n + 1)]
dp[1][1] = 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            continue
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        if (a[i - 1][j - 1] ^ k) == 0:
            dp[i][j] += 1
print(dp[n][m])

