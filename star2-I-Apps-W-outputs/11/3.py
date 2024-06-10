
from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(node, parent, graph, visited, cost):
    visited[node] = True
    for child in graph[node]:
        if child != parent:
            if not visited[child]:
                cost[child] = cost[node] + costs[child]
                dfs(child, node, graph, visited, cost)
            else:
                cost[child] = min(cost[child], cost[node] + costs[child])

n = int(input())
costs = list(map(int, input().split()))
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (n + 1)
cost = [float('inf')] * (n + 1)
cost[1] = costs[0]
dfs(1, -1, graph, visited, cost)
print(min(cost), cost.count(min(cost)))

