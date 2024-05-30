
def max_profit(n, k, a):
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[j][i] = max(dp[j][i-1], dp[j-1][i-1] + a[i-1])
    return dp[k][n]

def max_profit_dist(n, k, a):
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[j][i] = max(dp[j][i-1], dp[j-1][i-1] + a[i-1])
    ans = []
    j = k
    while j > 0:
        if dp[j][n] != dp[j-1][n]:
            ans.append(n)
            break
        else:
            ans.append(n-dp[j][n-dp[j][n]-1]+1)
            n -= dp[j][n]
            j -= 1
    return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(max_profit(n, k, a))
print(*max_profit_dist(n, k, a))

