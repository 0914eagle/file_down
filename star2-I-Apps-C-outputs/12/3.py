
def solve(d):
    n = len(d) + 1
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, 0, -1):
            dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + d[i - 1][j - 1]
    return dp[1][1]

n = int(input())
d = [list(map(int, input().split())) for _ in range(n - 1)]
print(solve(d))

