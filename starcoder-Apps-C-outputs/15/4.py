
def cal(N,C):
    if C>N*(N-1)//2:
        return 0
    dp = [[0]*(N+1) for _ in range(C+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(C+1):
            dp[j][i] += dp[j][i-1]
            if j>=i:
                dp[j][i] += dp[j-i][i-1]
                dp[j][i] %= 1000000007
    return dp[-1][-1]
