
from collections import defaultdict

def largest_S_size(n, m, edges):
    graph = defaultdict(list)
    indegree = [0] * n
    
    for edge in edges:
        x, y = edge
        graph[x].append(y)
        indegree[y] += 1
    
    sources = [node for node in range(n) if indegree[node] == 0]
    
    largest_S = max(len(sources), 1)
    
    return largest_S

# Input processing
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Output
print(largest_S_size(n, m, edges))
