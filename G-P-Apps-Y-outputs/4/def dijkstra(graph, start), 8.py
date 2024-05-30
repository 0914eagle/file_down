
def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        visited[u] = True
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist

n, m, k = map(int, input().split())
roads = []
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, w = map(int, input().split())
    roads.append((x-1, y-1, w))
    graph[x-1].append((y-1, w))
    graph[y-1].append((x-1, w))

courier_routes = []
for _ in range(k):
    a, b = map(int, input().split())
    courier_routes.append((a-1, b-1))

min_cost = float('inf')
for i in range(m):
    x, y, w = roads[i]
    graph[x].remove((y, w))
    graph[y].remove((x, w))
    
    dists = []
    for a, b in courier_routes:
        dist = dijkstra(graph, a)
        dists.append(dist[b])
    
    min_cost = min(min_cost, sum(dists))
    
    graph[x].append((y, w))
    graph[y].append((x, w))

print(min_cost)
```
