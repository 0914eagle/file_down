
n, k = map(int, input().split())
w = list(map(int, input().split()))
dp = [0] * (k+1)
dp[0] = 1
for weight in w:
  for j in range(k, weight-1, -1):
    dp[j] += dp[j-weight]
if dp[k] == 0:
  print(-1)
  print(0)
else:
  print(dp[k])
  dp2 = [0] * (k+1)
  dp2[0] = 1
  for weight in w:
    for j in range(k, weight-1, -1):
      dp2[j] += dp2[j-weight] * dp[j]
  print(dp2[k] % 1000000007)

