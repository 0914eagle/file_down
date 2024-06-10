
def solve(n, a):
    dp = [[0] * 2 for _ in range(n)]
    for i in range(n):
        if a[i] == 0:
            dp[i][0] = dp[i][1] = 0
        elif a[i] == 1:
            dp[i][0] = dp[i][1] = 1
        elif a[i] == 2:
            dp[i][0] = dp[i][1] = 1
        elif a[i] == 3:
            dp[i][0] = dp[i][1] = 2
        if i > 0:
            dp[i][0] = min(dp[i][0], dp[i - 1][1])
            dp[i][1] = min(dp[i][1], dp[i - 1][0])
    return min(dp[-1])

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

