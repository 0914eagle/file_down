
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1 if a[0][0] == k else 0
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i > 0:
            dp[i][j] += dp[i - 1][j] if (a[i][j] ^ a[i - 1][j]) == k else 0
        if j > 0:
            dp[i][j] += dp[i][j - 1] if (a[i][j] ^ a[i][j - 1]) == k else 0
print(dp[n - 1][m - 1])

