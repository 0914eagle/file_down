
# 对于每一个问号，都可以加加减减两种情况，而且问号的个数也是变化的，所以这个题可以用dp
import itertools
s = input()
r = input()
n = len(r)
a = r.count('+')
b = r.count('-')

dp = [[0 for i in range(2*n+1)] for j in range(n+1)]

if a == n:
    if r == s:
        print(1)
    else:
        print(0)
else:
    dp[0][n] = 1
    for i in range(n):
        for j in range(2*n+1):
            if dp[i][j] == 0:
                continue
            if r[i] == '-':
                dp[i+1][j-1] += dp[i][j]
            elif r[i] == '+':
                dp[i+1][j+1] += dp[i][j]
            else:
                dp[i+1][j-1] += dp[i][j]/2
                dp[i+1][j+1] += dp[i][j]/2
    print(dp[n][n-a+b])
