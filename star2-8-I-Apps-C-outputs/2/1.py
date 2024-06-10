
n, m = map(int, input().split())
graph = {i: set() for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
def independent_set(graph, v):
    if len(graph[v]) == 0:
        return 1
    result = 1
    for u in graph[v]:
        graph[u].discard(v)
        result = max(result, 1 + independent_set(graph, u))
        graph[u].add(v)
    return result
print(independent_set(graph, 1))

