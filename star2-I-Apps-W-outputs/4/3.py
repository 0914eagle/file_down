
def solve(n, a):
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = a[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + a[i]
    return max(dp[-1])

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

