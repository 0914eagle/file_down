
n, m = [int(i) for i in input().split()]
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = [int(i) for i in input().split()]
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def dfs(cur, visited, graph):
    visited.add(cur)
    for next_node in graph[cur]:
        if next_node not in visited:
            dfs(next_node, visited, graph)


def max_independent_set(graph):
    n = len(graph)
    visited = set()
    size = 0
    for i in range(n):
        if i not in visited:
            dfs(i, visited, graph)
            size += 1
    return size


print(max_independent_set(graph))

