
import heapq

def min_cut(graph, s, t):
    n = len(graph)
    visited = [False] * n
    visited[s] = True
    min_cut_edges = []
    
    pq = [(0, s)]
    while pq:
        weight, node = heapq.heappop(pq)
        if node == t:
            break
        
        for neighbor, edge_weight in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                heapq.heappush(pq, (edge_weight, neighbor))
                if neighbor != t:
                    min_cut_edges.append((node, neighbor))
    
    U = set()
    for edge in reversed(min_cut_edges):
        if edge[1] not in U:
            U.add(edge[0])
    
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
for node in U:
    print(node)
