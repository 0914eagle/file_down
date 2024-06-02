
import heapq

def min_cut(graph, s, t):
    n = len(graph)
    visited = [False] * n
    visited[s] = True
    min_cut_edges = []
    min_cut_vertices = set([s])
    
    pq = [(0, s)]
    while pq:
        weight, u = heapq.heappop(pq)
        for v, w in graph[u]:
            if not visited[v]:
                visited[v] = True
                min_cut_edges.append((u, v))
                min_cut_vertices.add(v)
                heapq.heappush(pq, (w, v))
    
    return min_cut_vertices

# Read input
n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# Find the minimum cut
min_cut_vertices = min_cut(graph, s, t)

# Output the result
print(len(min_cut_vertices))
for v in min_cut_vertices:
    print(v)
