
def max_independent_set(n, edges):
    def dfs(node, parent, included):
        size_included = 1
        size_excluded = 0
        
        for neighbor in edges[node]:
            if neighbor != parent:
                size_included += dfs(neighbor, node, False)
                if not included:
                    size_excluded += dfs(neighbor, node, True)
        
        return max(size_included, size_excluded)
    
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    return dfs(0, -1, True)

# Read input
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Call the function and Output the result
print(max_independent_set(n, edges))
```
