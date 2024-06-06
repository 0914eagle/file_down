
n, k = map(int, input().split())
a = input()
lst = []
for _ in range(n):
    lst.append(int(input()))
inf = 10000000000000
dp = [[[-inf]*2 for _ in range(k+1)] for _ in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    for j in range(k+1):
        dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][0])
        if j > 0:
            dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j-1][0]+lst[i])
            dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j-1][1]+lst[i])
            dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][1]+lst[i])
            dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j-1][0])
            dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j-1][1])
if dp[n][k][0] < -100000000:
    print('?')
else:
    print(max(dp[n][k][0], dp[n][k][1]))
