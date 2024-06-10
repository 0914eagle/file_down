
H, N = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
  A[i], B[i] = map(int, input().split())
dp = [float("inf")] * (H + 1)
dp[0] = 0
for i in range(H):
  for j in range(N):
    if i + A[j] <= H:
      dp[i + A[j]] = min(dp[i + A[j]], dp[i] + B[j])
print(dp[H])

