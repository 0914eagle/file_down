
def max_independent_set(n, edges):
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        adj_list[edge[0]-1].append(edge[1]-1)
        adj_list[edge[1]-1].append(edge[0]-1)

    dp = [[0, 1] for _ in range(n)]
    visited = [False] * n

    def dfs(node, parent):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor, node)
                dp[node][0] += dp[neighbor][1]
                dp[node][1] += min(dp[neighbor])

    dfs(0, -1)
    return max(dp[0])

# Input parsing
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Call the function and output the result
print(max_independent_set(n, edges))
```
