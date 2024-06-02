
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
    dist_from_s = dijkstra(graph, s)
    dist_from_t = dijkstra(graph, t)
    
    min_cut = float('inf')
    cut_vertex = -1
    
    for u in range(n):
        if dist_from_s[u] + dist_from_t[u] < min_cut:
            min_cut = dist_from_s[u] + dist_from_t[u]
            cut_vertex = u
    
    U = set()
    while cut_vertex != s:
        U.add(cut_vertex)
        for v, _ in graph[cut_vertex]:
            if dist_from_s[cut_vertex] == dist_from_s[v] + 1:
                cut_vertex = v
                break
    
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
