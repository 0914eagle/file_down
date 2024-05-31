
def minimal_sum_visible_fields(N, K, table):
    dp = [[1000000] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            for k in range(i):
                val = sum(table[l][i - 1] for l in range(k, i))
                dp[j][i] = min(dp[j][i], dp[j - 1][k] + val)

    return dp[K][N]

# Read input
N, K = map(int, input().split())
table = []
for _ in range(N):
    row = list(map(int, input().split()))
    table.append(row)

# Calculate and print the minimal sum of visible fields
result = minimal_sum_visible_fields(N, K, table)
print(result)
