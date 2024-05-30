
def max_independent_set(n, m, edges):
    adj_list = [[] for _ in range(n+1)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    dp = [[0, 0] for _ in range(n+1)]

    def dfs(node, parent):
        dp[node][1] = 1
        for child in adj_list[node]:
            if child != parent:
                dfs(child, node)
                dp[node][0] += max(dp[child][0], dp[child][1])
                dp[node][1] += dp[child][0]

    dfs(1, 0)
    return max(dp[1][0], dp[1][1])

# Read input
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print the result
print(max_independent_set(n, m, edges))
```
