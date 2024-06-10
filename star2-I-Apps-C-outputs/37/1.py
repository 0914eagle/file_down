
def solve(n, a):
    dp = [[0] * 4 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(4):
            if j == 0:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1], dp[i - 1][j + 2], dp[i - 1][j + 3])
            elif j == 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j + 1], dp[i - 1][j + 2]) + (a[i - 1] == 1 or a[i - 1] == 3)
            elif j == 2:
                dp[i][j] = min(dp[i - 1][j - 2], dp[i - 1][j - 1], dp[i - 1][j + 1]) + (a[i - 1] == 2 or a[i - 1] == 3)
            else:
                dp[i][j] = min(dp[i - 1][j - 3], dp[i - 1][j - 2], dp[i - 1][j - 1]) + (a[i - 1] == 3)
    return min(dp[n])

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

