
from sys import stdin
def bfs(graph, start):
    visited = [False]*len(graph)
    queue = [start]
    visited[start] = True
    while queue:
        node = queue.pop(0)
        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
    return visited
def beehive_colony(n, m, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    for i in range(n):
        if len(bfs(graph, i)) != n:
            return 'impossible'
    return n
n, m = map(int, stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    edges.append((u, v))
print(beehive_colony(n, m, edges))

