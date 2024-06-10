
n = int(input())
a = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for i in range(n):
    graph[a[i]-1].append(i)
def dfs(node, parent=-1):
    dp = [1, 0]
    for child in graph[node]:
        if child != parent:
            child_dp = dfs(child, node)
            dp[0] *= child_dp[1]
            dp[1] *= child_dp[0]
            dp[0] += dp[1]
            dp[1] += dp[0]
    dp[0] += dp[1]
    return dp
ans = 1
for i in range(n):
    if len(graph[i]) > 0:
        ans *= dfs(i)[1]
        ans %= 10**9 + 7
print(ans)

