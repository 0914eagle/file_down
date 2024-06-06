
n = int(input())
S = []
for _ in range(2 ** n):
    S.append(int(input()))
dp = [[0] * (n + 1) for _ in range(sum(S) + 1)]
dp[0][0] = 1
for i in range(2 ** n):
    for j in range(n + 1):
        if dp[S[i]][j]:
            dp[S[i]][j] = 2
for i in range(sum(S) + 1):
    if dp[i][0]:
        for j in range(n):
            if dp[i + S[j]][j + 1] == 2:
                dp[i + S[j]][j + 1] = 1
if dp[sum(S) - 1][-1] == 0:
    print('impossible')
    exit()
ans = []
for i in range(sum(S) + 1):
    if dp[i][-1] == 1:
        ans.append(i)
for i in range(n):
    print(ans[i + 1] - ans[i])
