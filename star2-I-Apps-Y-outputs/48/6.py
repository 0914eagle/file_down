
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * m for i in range(n)]
dp[0][0] = 1 if a[0][0] == k else 0
for i in range(n):
    for j in range(m):
        if i + 1 < n:
            dp[i + 1][j] += dp[i][j] if (a[i][j] ^ a[i + 1][j]) == k else 0
        if j + 1 < m:
            dp[i][j + 1] += dp[i][j] if (a[i][j] ^ a[i][j + 1]) == k else 0
print(dp[n - 1][m - 1])

