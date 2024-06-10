
def vasya_vacations(n, a):
    if n == 1:
        return 0
    if n == 2:
        if a[0] == 2 and a[1] == 2:
            return 1
        else:
            return 0
    dp = [[0] * 2 for _ in range(n)]
    if a[0] == 0 or a[0] == 1:
        dp[0][0] = 1
    if a[0] == 2 or a[0] == 3:
        dp[0][1] = 1
    if a[1] == 0 or a[1] == 1:
        dp[1][0] = dp[0][1] + 1
    if a[1] == 2 or a[1] == 3:
        dp[1][1] = dp[0][0] + 1
    for i in range(2, n):
        if a[i] == 0 or a[i] == 1:
            dp[i][0] = min(dp[i - 1][1], dp[i - 2][1]) + 1
        if a[i] == 2 or a[i] == 3:
            dp[i][1] = min(dp[i - 1][0], dp[i - 2][0]) + 1
    return min(dp[-1][0], dp[-1][1])

