
h,w=map(int,input().split())
r=list(map(int,input().split()))
c=list(map(int,input().split()))
if sum(r) != sum(c):
  print(0)
else:
  mod = 10**9+7
  dp = [[1]*(w+1) for i in range(h+1)]
  for i in range(1,h+1):
    for j in range(1,w+1):
      dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1])%mod
  ans = 1
  for i in range(h):
    ans = (ans*dp[r[i]][c[i]])%mod
  print(ans)

