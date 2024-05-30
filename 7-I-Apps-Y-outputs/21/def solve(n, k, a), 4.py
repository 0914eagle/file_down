
def solve(n, k, a):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + a[j - 1])
    ans = dp[-1][-1]
    days = [0] * k
    i, j = k, n
    while i > 0:
        days[i - 1] = j
        if dp[i][j] == dp[i - 1][j - 1] + a[j - 1]:
            j -= 1
        i -= 1
    return ans, days

