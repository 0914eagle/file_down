
from sys import stdin
input_str = stdin.read()
def solve(input_str):
    n = len(input_str)
    dp = [[-1 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(n+1):
            if input_str[i-1] == '1':
                dp[i][j] = dp[i-1][j]
            else:
                if dp[i-1][j] == -1:
                    dp[i][j] = -1
                else:
                    dp[i][j] = dp[i-1][j] + 1
            if j > 0:
                if dp[i-1][j-1] == -1:
                    continue
                if input_str[i-1] == '1':
                    if dp[i][j] == -1 or dp[i-1][j-1] < dp[i][j]:
                        dp[i][j] = dp[i-1][j-1]
                else:
                    if dp[i][j] == -1 or dp[i-1][j-1] + 1 < dp[i][j]:
                        dp[i][j] = dp[i-1][j-1] + 1
    for i in range(n+1):
        if dp[n][i] != -1:
            return dp[n][i]
print(solve(input_str))

