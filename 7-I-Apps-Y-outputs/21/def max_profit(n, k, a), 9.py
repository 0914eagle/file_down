

def max_profit(n, k, a):
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+a[i-1])
    return dp[-1][-1]

def solve(n, k, a):
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+a[i-1])
    ans = []
    i = n
    j = k
    while i > 0:
        if dp[i-1][j] < dp[i-1][j-1] + a[i-1]:
            ans.append(i)
            i -= 1
            j -= 1
        else:
            i -= 1
    return ans


n, k = map(int, input().split())
a = list(map(int, input().split()))
print(max_profit(n, k, a))
print(*solve(n, k, a))

