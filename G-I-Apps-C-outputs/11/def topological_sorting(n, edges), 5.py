
def topological_sorting(n, edges):
    in_degree = [0] * n
    adj_list = [[] for _ in range(n)]
    
    # Create the adjacency list and calculate the in-degree of each node
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        in_degree[v] += 1
    
    # Initialize the set of source nodes
    sources = [node for node in range(n) if in_degree[node] == 0]
    
    # Initialize the maximum size of S seen so far
    max_size_S = len(sources)
    
    for source in sources:
        for neighbor in adj_list[source]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                sources.append(neighbor)
        
        max_size_S = max(max_size_S, len(sources))
    
    return max_size_S

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

print(topological_sorting(n, edges))
```
