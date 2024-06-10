
import sys
sys.setrecursionlimit(10**6)

def dfs(u, p):
    global cost, dp, ways
    dp[u] = cost[u]
    ways[u] = 1
    for v in graph[u]:
        if v != p:
            dfs(v, u)
            dp[u] += dp[v]
            ways[u] *= ways[v]
            ways[u] %= 10**9 + 7

n = int(input())
cost = list(map(int, input().split()))
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
dp = [0] * (n + 1)
ways = [1] * (n + 1)
dfs(1, 0)
print(dp[1], ways[1])

