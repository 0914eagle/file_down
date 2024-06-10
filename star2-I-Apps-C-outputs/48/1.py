
def maximal_factoring(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if l == 1:
                dp[i][j] = 1
            else:
                for k in range(i, j):
                    if s[k] == s[j]:
                        dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)
            if dp[i][j] == 0:
                dp[i][j] = l
    return dp[0][n - 1]

s = input()
print(maximal_factoring(s))

