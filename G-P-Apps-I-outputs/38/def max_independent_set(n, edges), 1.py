
def max_independent_set(n, edges):
    graph = {}
    for i in range(n):
        graph[i + 1] = set()
    
    for edge in edges:
        a, b = edge
        graph[a].add(b)
        graph[b].add(a)
    
    def dfs(node, parent, include_node):
        if include_node:
            count = 1
            for child in graph[node]:
                if child != parent:
                    count += dfs(child, node, False)
            return count
        else:
            count = 0
            for child in graph[node]:
                if child != parent:
                    count += dfs(child, node, True)
            return count
    
    return max(dfs(1, 0, True), dfs(1, 0, False))

# Input reading
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(max_independent_set(n, edges))
```
