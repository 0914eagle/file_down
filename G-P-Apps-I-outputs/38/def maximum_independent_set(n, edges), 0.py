
def maximum_independent_set(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    def dfs(node, parent, taken):
        without_node = 0
        with_node = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                without_node += dfs(neighbor, node, False)
        if not taken:
            for neighbor in graph[node]:
                if neighbor != parent:
                    with_node += dfs(neighbor, node, True)
        return max(without_node, with_node)

    return dfs(0, -1, False)

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function with the input
result = maximum_independent_set(n, edges)
print(result)
```
