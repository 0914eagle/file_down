
import heapq

def min_cut(graph, s, t):
    n = len(graph)
    dist = [float('inf')] * n
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    U = set()
    for i in range(n):
        if i != t and dist[i] < float('inf'):
            U.add(i)
    
    return U

# Read input
n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# Find the minimum cut
U = min_cut(graph, s, t)

# Output the result
print(len(U))
for u in U:
    print(u)
