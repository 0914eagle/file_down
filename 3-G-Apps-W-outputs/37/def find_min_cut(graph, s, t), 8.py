
import heapq

def find_min_cut(graph, s, t):
    n = len(graph)
    visited = [False] * n
    min_cut = set()
    min_cut.add(s)
    min_heap = [(0, s)]

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True

        for neighbor, edge_weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor))

        if node == t:
            break

    for i in range(n):
        if not visited[i]:
            min_cut.add(i)

    return min_cut

# Read input
n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# Find min cut
min_cut = find_min_cut(graph, s, t)

# Output
print(len(min_cut))
for node in min_cut:
    print(node)
