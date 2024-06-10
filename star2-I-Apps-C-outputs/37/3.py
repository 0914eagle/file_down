
def solve(n, a):
    dp = [0] * n
    for i in range(n):
        if a[i] == 0:
            dp[i] = 0
        elif a[i] == 1:
            dp[i] = 1
        elif a[i] == 2:
            dp[i] = 1
        elif a[i] == 3:
            dp[i] = 2
        if i > 0:
            dp[i] = min(dp[i], dp[i - 1] + 1)
    return dp[n - 1]


n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

