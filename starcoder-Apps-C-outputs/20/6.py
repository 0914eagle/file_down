
def solve(s):
    dp = [[0]*2 for i in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(2):
            if s[i] == s[i-1] or (j == 1 and s[i-1] == 'A' and s[i] == 'B'):
                dp[i][j] = 1 + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n-1][1]
    
n = int(input())
s = input()
print(solve(s))
