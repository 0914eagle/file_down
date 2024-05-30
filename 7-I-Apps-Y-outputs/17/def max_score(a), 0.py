
def max_score(a):
    n = len(a)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]
    for i in range(n-1):
        dp[i][i+1] = max(a[i], a[i+1])
    for i in range(n-2, -1, -1):
        for j in range(i+2, n):
            dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1])
    return dp[0][-1] - dp[-1][0]

