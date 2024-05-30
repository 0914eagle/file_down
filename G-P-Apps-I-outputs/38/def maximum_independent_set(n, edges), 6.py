
def maximum_independent_set(n, edges):
    graph = {}
    for i in range(1, n+1):
        graph[i] = set()
    
    for edge in edges:
        a, b = edge
        graph[a].add(b)
        graph[b].add(a)
    
    def dfs(node, parent, include_node):
        if include_node:
            size = 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    size += dfs(neighbor, node, False)
            return size
        else:
            size_with_node = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    size_with_node += dfs(neighbor, node, True)
            size_without_node = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    size_without_node += dfs(neighbor, node, False)
            return max(size_with_node, size_without_node)
    
    return dfs(1, -1, True)

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and output the result
print(maximum_independent_set(n, edges))
```
