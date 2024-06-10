
import sys

def solve(n, m, edges):
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    visited = [False] * (n + 1)
    
    def dfs(u, depth):
        visited[u] = True
        max_depth = depth
        for v in graph[u]:
            if not visited[v]:
                max_depth = max(max_depth, dfs(v, depth + 1))
        return max_depth
    
    return dfs(1, 0) + 1

n, m = map(int, input().split())
edges = [tuple(map(int, line.split())) for line in sys.stdin.readlines()]
print(solve(n, m, edges))

