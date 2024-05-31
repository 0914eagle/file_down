
def minimal_sum_visible_fields(N, K, table):
    dp = [[[float('inf')] * (K + 1) for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = 0
    
    for r in range(N):
        for c in range(N):
            for k in range(K + 1):
                if c > 0:
                    dp[r][c][k] = min(dp[r][c][k], dp[r][c - 1][k])
                if r > 0:
                    dp[r][c][k] = min(dp[r][c][k], dp[r - 1][c][k])
                
                if k > 0:
                    if c > 0:
                        dp[r][c][k] = min(dp[r][c][k], dp[r][c - 1][k - 1] + table[r][c])
                    if r > 0:
                        dp[r][c][k] = min(dp[r][c][k], dp[r - 1][c][k - 1] + table[r][c])
    
    return dp[N - 1][N - 1][K]

# Input processing
N, K = map(int, input().split())
table = []
for _ in range(N):
    row = list(map(int, input().split()))
    table.append(row)

result = minimal_sum_visible_fields(N, K, table)
print(result)
