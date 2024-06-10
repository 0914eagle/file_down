
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent):
    dp[node][0] = 0
    dp[node][1] = cost[node]
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])

n = int(input())
cost = list(map(int, input().split()))
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
dp = [[0, 0] for _ in range(n+1)]
dfs(1, -1)
print(min(dp[1][0], dp[1][1]), 1 if dp[1][0] < dp[1][1] else 2)
