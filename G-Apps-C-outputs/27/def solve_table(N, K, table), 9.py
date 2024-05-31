
def solve_table(N, K, table):
    dp = [[float('inf')] * N for _ in range(K + 1)]
    dp[0][0] = 0

    for i in range(N):
        for k in range(1, K + 1):
            for j in range(i + 1):
                dp[k][i] = min(dp[k][i], dp[k - 1][j] + sum(table[j][l] for l in range(i + 1)))

    return dp[K][N - 1]

# Reading input
N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# Solving and printing the result
print(solve_table(N, K, table))
