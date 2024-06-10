
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
    max_k = 1
    for l in range(n, 0, -1):
        for i in range(n - l + 1):
            if dp[i][i + l - 1] == 1:
                max_k = max(max_k, l)
    return max_k

s = input()
print(solve(s))

