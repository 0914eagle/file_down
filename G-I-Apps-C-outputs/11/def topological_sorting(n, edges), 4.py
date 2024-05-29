
def topological_sorting(n, edges):
    in_degree = [0] * n
    graph = {i: [] for i in range(n)}

    for edge in edges:
        u, v = edge
        graph[u].append(v)
        in_degree[v] += 1

    sources = [node for node in range(n) if in_degree[node] == 0]
    max_sources = 0

    while sources:
        if len(sources) > max_sources:
            max_sources = len(sources)

        new_sources = []
        for source in sources:
            for neighbor in graph[source]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    new_sources.append(neighbor)

        sources = new_sources

    return max_sources

# Read input
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Call the function and output the result
print(topological_sorting(n, edges))
```
