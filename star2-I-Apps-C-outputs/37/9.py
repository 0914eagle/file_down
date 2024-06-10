
def solve(n, a):
    dp = [[0] * 4 for _ in range(n)]
    for i in range(n):
        if i == 0:
            if a[i] == 0:
                dp[i][0] = 1
            elif a[i] == 1:
                dp[i][1] = 1
            elif a[i] == 2:
                dp[i][2] = 1
            elif a[i] == 3:
                dp[i][3] = 1
        else:
            if a[i] == 0:
                dp[i][0] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i - 1][3]) + 1
            elif a[i] == 1:
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i - 1][3]) + 1
            elif a[i] == 2:
                dp[i][2] = min(dp[i - 1][0], dp[i - 1][2]) + 1
            elif a[i] == 3:
                dp[i][3] = min(dp[i - 1][1], dp[i - 1][3]) + 1
    return min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2], dp[n - 1][3])

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

