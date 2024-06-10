
from sys import stdin
def dfs(i):
    if i == n:
        return 0
    ans = 0
    if dp[i] != -1:
        return dp[i]
    for j in range(i, n):
        if r[j] > 1:
            ans = max(ans, dfs(j + 1) + q[j] / r[j])
        else:
            ans = max(ans, dfs(j + 1) + q[j])
    dp[i] = ans
    return ans
n = int(stdin.readline())
q, r = [0] * n, [0] * n
for i in range(n):
    o, w, r[i] = stdin.readline().split()
    if o == "pink":
        q[i] = 1
dp = [-1] * n
ans = dfs(0)
print("%.10f" % min(ans, 10))

