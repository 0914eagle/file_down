
def max_sum(a, k):
    n, m = len(a), len(a[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            if j > 1 and a[i - 1][j - 2] % k == 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + a[i - 1][j - 2])
    return dp[n][m]

