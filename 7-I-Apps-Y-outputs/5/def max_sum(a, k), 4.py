
def max_sum(a, k):
    n, m = len(a), len(a[0])
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if j == 0:
                dp[i][j] = a[i][j]
            else:
                dp[i][j] = max(dp[i][j - 1], a[i][j] + dp[i][j - 1])
    max_sum = 0
    for i in range(n):
        for j in range(m // 2 + 1):
            if dp[i][j] % k == 0:
                max_sum = max(max_sum, dp[i][j])
    return max_sum

