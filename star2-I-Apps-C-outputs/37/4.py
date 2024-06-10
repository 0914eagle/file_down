
def solve(n, a):
    if n == 1:
        return 0
    if n == 2:
        if a[0] == 2 and a[1] == 2:
            return 1
        else:
            return 0
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = 1
    dp[1][0] = 1
    dp[1][1] = 0
    for i in range(2, n):
        if a[i] == 2:
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = min(dp[i - 2][0], dp[i - 2][1]) + 1
        else:
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + 1
            dp[i][1] = min(dp[i - 2][0], dp[i - 2][1])
    return min(dp[n - 1][0], dp[n - 1][1])

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

