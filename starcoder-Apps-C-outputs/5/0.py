
n = int(input())
a = [int(x) for x in input().split()]
a.append(10000000000000000)
dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
dp[n - 1][1] = a[n - 1]
for i in range(n - 2, -1, -1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i + 1][j]
        if j - 1 > 0:
            dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + min(a[i], a[i + 1]))
        if j + 1 <= n:
            dp[i][j] = max(dp[i][j], dp[i + 1][j + 1] + min(a[i], a[i + 1]))
print(dp[0][n])
