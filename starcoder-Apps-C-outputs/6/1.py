
dp=[0 for i in range(n)]
for i in range(n):
    dp[i]=int(input())
    temp=int(input())
    for j in range(temp):
        l,k=map(int,input().split())
        dp[i]=min(dp[i],dp[k]+l)
print(dp[0])
