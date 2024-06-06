
n = int(input())
dp = [0 for i in range(n + 1)]
lst = [list(map(int, input().split())) for i in range(n)]
dp[1] = lst[0][0]
for i in range(2, n + 1):
    v, p = lst[i - 1]
    dp[i] = max(dp[i - 1], v + dp[p])
print(max(dp))
