
def maximum_independent_set_size(n, edges):
    graph = {i: set() for i in range(1, n + 1)}
    for edge in edges:
        a, b = edge
        graph[a].add(b)
        graph[b].add(a)

    def dfs(u, parent, dp):
        incl = 1
        excl = 0
        for v in graph[u]:
            if v != parent:
                dfs(v, u, dp)
                incl += dp[v][1]
                excl += max(dp[v][0], dp[v][1])
        dp[u] = (incl, excl)

    dp = {}
    dfs(1, -1, dp)
    return max(dp[1])

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and output the maximum independent set size
print(maximum_independent_set_size(n, edges))
```
