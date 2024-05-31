
def minimal_sum_of_visible_fields(N, K, table):
    dp = [[[float('inf')] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            dp[i][j][0] = table[i][j]
    
    for k in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                for di, dj in [(0, 1), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if ni < N and nj < N:
                        dp[ni][nj][k] = min(dp[ni][nj][k], dp[i][j][k-1])
    
    return dp[N-1][N-1][K]

# Reading input
N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# Calling the function and printing the result
result = minimal_sum_of_visible_fields(N, K, table)
print(result)
