
def maximum_independent_set_size(n, m, edges):
    adj_list = [[] for _ in range(n+1)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    visited = [False] * (n+1)
    independent_set = 0

    def dfs(node, parent):
        nonlocal independent_set
        take_node = 1
        skip_node = 0
        for neighbor in adj_list[node]:
            if neighbor != parent:
                dfs(neighbor, node)
                take_node += visited[neighbor]
                skip_node += max(visited[neighbor])

        visited[node] = max(take_node, skip_node)
        independent_set = max(independent_set, visited[node])

    dfs(1, 0)
    return independent_set

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = maximum_independent_set_size(n, m, edges)
print(result)
```
