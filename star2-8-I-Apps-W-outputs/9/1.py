
h, n = map(int, input().split())
a = []
b = []
for i in range(n):
  ai, bi = map(int, input().split())
  a.append(ai)
  b.append(bi)
dp = [float("inf")] * (h + 1)
dp[0] = 0
for i in range(1, h + 1):
  for j in range(n):
    if i - a[j] >= 0:
      dp[i] = min(dp[i], dp[i - a[j]] + b[j])
print(dp[h])

