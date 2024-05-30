


def solve(n, k, a):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + a[j - 1], dp[i][j - 1])
    return dp[k][n]


def solve_2(n, k, a):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + a[j - 1], dp[i][j - 1])
    ans = []
    i, j = k, n
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j - 1] + a[j - 1]:
            ans.append(j)
            i -= 1
            j -= 1
        else:
            j -= 1
    return dp[k][n], ans


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
    print(solve_2(n, k, a)[1])

