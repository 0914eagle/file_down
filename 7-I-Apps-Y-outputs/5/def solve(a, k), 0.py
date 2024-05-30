
def solve(a, k):
    n, m = len(a), len(a[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i + 1][j + 1])
            if j + 1 <= m // 2:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i][j])
    return max(dp[-1])

