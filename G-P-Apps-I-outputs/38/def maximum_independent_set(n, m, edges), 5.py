
def maximum_independent_set(n, m, edges):
    graph = {i: set() for i in range(1, n+1)}
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    independent_set = set()
    for vertex in range(1, n+1):
        if all(neighbour not in independent_set for neighbour in graph[vertex]):
            independent_set.add(vertex)

    return len(independent_set)

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Find maximum independent set
result = maximum_independent_set(n, m, edges)
print(result)
```
