
def min_sum_visible_fields(N, K, table):
    dp = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            dp[i][j] = table[i][j]
    
    for _ in range(K):
        new_dp = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                new_dp[i][j] = dp[i][j]
                if i > 0:
                    new_dp[i][j] = min(new_dp[i][j], dp[i-1][j] + table[i][j])
                if j > 0:
                    new_dp[i][j] = min(new_dp[i][j], dp[i][j-1] + table[i][j])
                if i < N - 1:
                    new_dp[i][j] = min(new_dp[i][j], dp[i+1][j] + table[i][j])
                if j < N - 1:
                    new_dp[i][j] = min(new_dp[i][j], dp[i][j+1] + table[i][j])
        dp = new_dp

    return dp[N-1][N-1]

# Input processing
N, K = map(int, input().split())
table = []
for _ in range(N):
    row = list(map(int, input().split()))
    table.append(row)

result = min_sum_visible_fields(N, K, table)
print(result)
