
n,k = map(int,input().split())

dp = [0] * (n+1)
dp[0] = k
dp[1] = k * (k-1)

for i in range(2,n):
    dp[i] = (dp[i-1] + dp[i-2]) * (k-1)

print(dp[n-1])

