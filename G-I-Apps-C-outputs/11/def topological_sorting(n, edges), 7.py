
def topological_sorting(n, edges):
    graph = {i: [] for i in range(n)}
    in_degree = [0] * n
    for x, y in edges:
        graph[x].append(y)
        in_degree[y] += 1
    
    source_nodes = [node for node in graph if in_degree[node] == 0]
    max_source_nodes = 0

    while source_nodes:
        max_source_nodes = max(max_source_nodes, len(source_nodes))
        new_source_nodes = []
        
        for node in source_nodes:
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    new_source_nodes.append(neighbor)
        
        source_nodes = new_source_nodes

    return max_source_nodes

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function with the input data
result = topological_sorting(n, edges)

# Output the result
print(result)
