
def solve(n, a):
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = 0 if a[0] == 0 or a[0] == 1 else 1
    dp[0][1] = 0 if a[0] == 2 or a[0] == 3 else 1
    for i in range(1, n):
        if a[i] == 0 or a[i] == 1:
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][1])
        else:
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + 1
        if a[i] == 2 or a[i] == 3:
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1])
        else:
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + 1
    return min(dp[-1][0], dp[-1][1])

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

