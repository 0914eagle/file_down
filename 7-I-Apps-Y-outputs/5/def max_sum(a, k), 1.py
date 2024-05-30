
def max_sum(a, k):
    n, m = len(a), len(a[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if a[i - 1][j - 1] % k == 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + a[i - 1][j - 1])
    return dp[n][m]


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    print(max_sum(a, k))

