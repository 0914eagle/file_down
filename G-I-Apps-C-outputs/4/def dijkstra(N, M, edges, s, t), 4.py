
from collections import deque

def dijkstra(N, M, edges, s, t):
    dist = [float('inf')] * N
    dist[s] = 0
    visited = [False] * N
    parent = [-1] * N
    queue = deque([s])

    while queue:
        u = queue.popleft()
        visited[u] = True
        for v, w in edges[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                if not visited[v]:
                    queue.append(v)

    path = []
    current = t
    while current != -1:
        path.append(current)
        current = parent[current]

    return path[::-1]

if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges[u].append((v, w))

    s, t = map(int, input().split())

    path = dijkstra(N, M, edges, s, t)

    print(' '.join(map(str, path)))
```
