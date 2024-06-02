
import heapq

def min_cut(graph, s, t):
    n = len(graph)
    visited = [False] * n
    min_cut_set = set()
    
    def dijkstra():
        nonlocal min_cut_set
        pq = [(0, s)]
        while pq:
            dist, node = heapq.heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            if node != s:
                min_cut_set.add(node)
            for neighbor, weight in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(pq, (dist + weight, neighbor))
    
    dijkstra()
    
    return min_cut_set

# Read input
n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# Find the minimum cut
min_cut_set = min_cut(graph, s, t)

# Output the result
print(len(min_cut_set))
for node in min_cut_set:
    print(node)
