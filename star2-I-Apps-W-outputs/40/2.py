
def ktree(n, k, d):
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(d, k+1):
        dp[i][i] = 1
    for i in range(d, k+1):
        for j in range(i+1, n+1):
            dp[i][j] = sum(dp[i-1][j-i:j])
    return sum(dp[i][n] for i in range(d, k+1)) % 1000000007

n, k, d = map(int, input().split())
print(ktree(n, k, d))

