

def max_sum(a, k):
    n, m = len(a), len(a[0])
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j] = a[i][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i][j - 1]
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            dp[i][j] %= k
    ans = 0
    for i in range(n):
        for j in range(m):
            if j - 1 >= 0:
                ans = max(ans, dp[i][j] - dp[i][j - 1])
            if i - 1 >= 0:
                ans = max(ans, dp[i][j] - dp[i - 1][j])
    return ans



