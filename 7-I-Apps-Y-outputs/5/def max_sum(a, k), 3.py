

def max_sum(a, k):
    n, m = len(a), len(a[0])
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if j == 0:
                dp[i][j] = a[i][j]
            else:
                dp[i][j] = max(dp[i][j - 1], a[i][j])
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if j == m - 1:
                dp[i][j] = dp[i][j] + dp[i][j - 1] - a[i][j]
            else:
                dp[i][j] = max(dp[i][j], dp[i][j + 1]) + a[i][j]
    ans = 0
    for i in range(n):
        for j in range(m // 2):
            if dp[i][j] % k == 0:
                ans = max(ans, dp[i][j])
    return ans



