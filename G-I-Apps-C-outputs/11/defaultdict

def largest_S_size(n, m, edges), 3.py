
from collections import defaultdict

def largest_S_size(n, m, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    for edge in edges:
        x, y = edge
        graph[x].append(y)
        indegree[y] += 1

    sources = [node for node in range(n) if indegree[node] == 0]
    max_source_size = len(sources)

    return max_source_size

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function
result = largest_S_size(n, m, edges)

# Output the result
print(result)
