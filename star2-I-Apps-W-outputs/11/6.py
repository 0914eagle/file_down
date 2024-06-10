
from collections import defaultdict

def dfs(node, parent, graph, visited, cost):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            cost[child] = cost[node] + graph[node][child]
            dfs(child, node, graph, visited, cost)


def solve(n, cost, m, roads):
    graph = defaultdict(dict)
    for u, v in roads:
        graph[u][v] = 1
        graph[v][u] = 1
    
    visited = [False] * (n + 1)
    cost = [0] * (n + 1)
    
    dfs(1, -1, graph, visited, cost)
    
    min_cost = float('inf')
    ways = 0
    
    for i in range(1, n + 1):
        if cost[i] < min_cost:
            min_cost = cost[i]
            ways = 1
        elif cost[i] == min_cost:
            ways += 1
    
    return min_cost, ways

n = int(input())
cost = list(map(int, input().split()))
m = int(input())
roads = [list(map(int, input().split())) for _ in range(m)]

min_cost, ways = solve(n, cost, m, roads)
print(min_cost, ways)

