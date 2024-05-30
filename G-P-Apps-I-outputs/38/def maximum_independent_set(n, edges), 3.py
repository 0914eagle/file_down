
def maximum_independent_set(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    def dfs(node, parent, dp):
        if dp[node][0] != -1:
            return dp[node]
        
        size_include = 1
        size_exclude = 0
        
        for neighbor in graph[node]:
            if neighbor != parent:
                size_include += dfs(neighbor, node, dp)[1]
                size_exclude += dfs(neighbor, node, dp)[0]
        
        dp[node] = (size_include, size_exclude)
        return dp[node]
    
    dp = [(-1, -1) for _ in range(n)]
    result = dfs(0, -1, dp)
    
    return max(result)

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and output the result
print(maximum_independent_set(n, edges))
```
