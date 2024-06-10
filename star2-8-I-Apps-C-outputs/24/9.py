
import math

def dist(x1, y1, x2, y2):
  return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

x_roost, y_roost = map(float, input().split())
N = int(input())
x_hides = []
y_hides = []
for _ in range(N):
  x, y = map(float, input().split())
  x_hides.append(x)
  y_hides.append(y)
x_hides.append(x_roost)
y_hides.append(y_roost)
dist_mat = [[0.0] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
  for j in range(N + 1):
    dist_mat[i][j] = dist(x_hides[i], y_hides[i], x_hides[j], y_hides[j])
dp = [[0.0] * (N + 1) for _ in range(1 << (N + 1))]
for mask in range(1, 1 << (N + 1)):
  dp[mask][0] = float('inf')
  for i in range(1, N + 1):
    if mask & (1 << i):
      for j in range(N + 1):
        if mask & (1 << j) and dp[mask ^ (1 << i)][j] + dist_mat[j][i] < dp[mask][i]:
          dp[mask][i] = dp[mask ^ (1 << i)][j] + dist_mat[j][i]

ans = float('inf')
for i in range(1, N + 1):
  ans = min(ans, dp[(1 << (N + 1)) - 1][i] + dist_mat[i][0])
print(ans)

