
# 该题的关键是 我们可以把距离做一个二维数组, 然后在对这个二维数组进行dp
# 如果能到达(i,j) 那么我们可以得到一个状态转移方程 dp[i][j] = min(dp[i][j-1], dp[i-1][j-1]+(j-i-1)*a[i][1]+a[i][0])

n,g = map(int,input().split())
dp = [[0 for i in range(200005)]for j in range(n)]
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    dp[i][0] = 10000000000000000000000000
for i in range(1,n):
    dp[0][i] = 10000000000000000000000000
dp[0][0] = 0
for i in range(1,n):
    for j in range(1,g+1):
        if j<i+1:
            dp[i][j] = 10000000000000000000000000
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+(j-i-1)*a[i][1]+a[i][0])
if dp[n-1][g]>=10000000000000000000000000:
    print('cancel road trip')
else:
    print(dp[n-1][g])
