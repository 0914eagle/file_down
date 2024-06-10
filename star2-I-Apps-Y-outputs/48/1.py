
n, m, k = map(int, input().split())
a = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    a[i][1:] = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[1][1] = 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            continue
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        if (a[i][j] ^ k) == k:
            dp[i][j] += 1
print(dp[n][m])

