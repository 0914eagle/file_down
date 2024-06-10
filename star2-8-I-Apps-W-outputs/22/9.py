

n = int(input())
a = list(map(int, input().split()))
a = [0] + a
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i].append(a[i])
parent = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
def dfs(node, par):
    visited[node] = True
    parent[node] = par
    for child in graph[node]:
        if visited[child]:
            if child != par:
                return child
        else:
            cycle_node = dfs(child, node)
            if cycle_node:
                return cycle_node
for i in range(1, n + 1):
    if not visited[i]:
        cycle_node = dfs(i, 0)
        if cycle_node:
            break
ans = pow(2, n, 10**9 + 7)
if cycle_node:
    ans -= pow(2, n - 1, 10**9 + 7)
print(ans)


