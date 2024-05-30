
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
    res = 0
    for i in range(n):
        for j in range(m // 2):
            res = max(res, dp[i][j] + dp[i][m - 1 - j])
    return res


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = [[int(x) for x in input().split()] for _ in range(n)]
    print(max_sum(a, k))

