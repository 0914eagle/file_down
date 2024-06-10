
def solve(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and (l == 2 or dp[i + 1][j - 1] == 1):
                dp[i][j] = 1
    max_len = 1
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if dp[i][j] == 1:
                max_len = max(max_len, l)
    return max_len

