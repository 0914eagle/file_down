

def solve(n, k, weights):
  dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
  for i in range(1, n + 1):
    for j in range(1, k + 1):
      if j >= weights[i - 1]:
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - weights[i - 1]]
      else:
        dp[i][j] = dp[i - 1][j]
  return dp[-1][-1]


n, k = map(int, input().split())
weights = list(map(int, input().split()))
print(solve(n, k, weights))


