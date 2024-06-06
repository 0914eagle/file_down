
def min_disparity(n, d):
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + d[i][j]
    return dp[0][0]

n = int(input())
d = []
for i in range(n - 1):
    d.append(list(map(int, input().split())))
print(min_disparity(n, d))
