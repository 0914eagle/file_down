
import heapq

def find_min_cut(graph, s, t):
    n = len(graph)
    visited = [False] * n
    min_cut = set()
    
    min_heap = [(0, s)]
    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        min_cut.add(node)
        
        for neighbor, edge_weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor))
    
    min_cut.remove(t)
    return min_cut

# Read input
n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# Find the minimum cut
min_cut = find_min_cut(graph, s, t)

# Output the result
print(len(min_cut))
for node in min_cut:
    print(node)
