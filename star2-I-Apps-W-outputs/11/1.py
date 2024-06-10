
from collections import defaultdict
def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)
def solve(n, costs, m, roads):
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
    visited = [False] * (n + 1)
    dfs(1, visited, graph)
    if not all(visited):
        return -1, -1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = costs[i - 1]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    ways = 1
    min_cost = sum(dp[i][i] for i in range(1, n + 1))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] == dp[i][i] + dp[j][j]:
                ways *= 2
                ways %= 1000000007
    return min_cost, ways
n = int(input())
costs = list(map(int, input().split()))
m = int(input())
roads = [list(map(int, input().split())) for _ in range(m)]
min_cost, ways = solve(n, costs, m, roads)
print(min_cost, ways)

