
import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist

def find_min_cut(graph, s, t):
    n = len(graph)
    dist_s = dijkstra(graph, s)
    dist_t = dijkstra(graph, t)
    
    U = set()
    for i in range(n):
        if dist_s[i] < float('inf') and dist_t[i] > dist_s[i]:
            U.add(i)
    
    return U

# Read input
n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# Find the minimum cut
U = find_min_cut(graph, s, t)

# Output the result
print(len(U))
for u in U:
    print(u)
