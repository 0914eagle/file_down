
def min_visible_sum(N, K, table):
    dp = [[float('inf')] * (N+1) for _ in range(K+1)]
    dp[0][0] = 0

    for i in range(1, N+1):
        for j in range(1, K+1):
            dp[j][i] = min(dp[j][i], dp[j][i-1] + table[i-1][0] + table[i-1][1])
            if i > 1:
                dp[j][i] = min(dp[j][i], dp[j-1][i-2] + table[i-1][0] + table[i-2][0])
            if j > 1:
                dp[j][i] = min(dp[j][i], dp[j-2][i-1] + table[i-1][0] + table[i-1][1])

    return dp[K][N]

# Input
N, K = map(int, input().split())
table = []
for _ in range(N):
    row = list(map(int, input().split()))
    table.append(row)

# Output
print(min_visible_sum(N, K, table))
