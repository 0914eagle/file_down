
'''
2022-07-02-22:51:26
'''

n, s, m, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [[10**10] * (m+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(s):
        l, r = map(int, input().split())
        for q in range(m+1):
            dp[i][q] = min(dp[i][q], dp[i-1][q], dp[l-1][q] + 1)
        for q in range(1, m+1):
            dp[i][q] = min(dp[i][q], dp[l-1][q-1] + 1)

res = 10**10
for i in range(m, n+1):
    res = min(res, dp[n][i])
if res == 10**10:
    res = -1
print(sorted(a)[k-1] if res >= k else -1)
