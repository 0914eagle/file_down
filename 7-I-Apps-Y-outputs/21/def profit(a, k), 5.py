

def profit(a, k):
    dp = [[0] * (k + 1) for _ in range(len(a))]
    for i in range(1, len(a)):
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i])
    return dp[-1][-1]

def solution(a, k):
    dp = [[0] * (k + 1) for _ in range(len(a))]
    for i in range(1, len(a)):
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i])
    res = []
    i, j = len(a) - 1, k
    while i > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            res.append(i)
            i -= 1
            j -= 1
    return dp[-1][-1], res[::-1]



