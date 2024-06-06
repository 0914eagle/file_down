
mod=1000000007
n,c=map(int,input().split())
if n==1:
    print(0)
else:
    dp=[[0 for i in range(1001)] for i in range(1001)]
    dp[0][0]=1
    for i in range(1,n):
        for j in range(i):
            for k in range(c+1):
                if k>=i:
                    dp[i][k]=(dp[i][k]+dp[i-1][k-i]*(i-1))%mod
                else:
                    dp[i][k]=(dp[i][k]+dp[i-1][k])%mod
    print(dp[n-1][c])
