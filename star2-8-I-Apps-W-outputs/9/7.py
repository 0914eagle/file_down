
H, N = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
dp = [[float('inf')] * (H+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(H+1):
        if dp[i][j] < float('inf'):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            dp[i+1][min(j+A[i], H)] = min(dp[i+1][min(j+A[i], H)], dp[i][j]+B[i])
ans = float('inf')
for i in range(H+1):
    if dp[N][i] < float('inf'):
        ans = min(ans, dp[N][i])
print(ans)

