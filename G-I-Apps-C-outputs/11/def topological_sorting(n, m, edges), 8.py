
def topological_sorting(n, m, edges):
    graph = {i: [] for i in range(n)}
    in_degrees = [0] * n

    for edge in edges:
        x, y = edge
        graph[x].append(y)
        in_degrees[y] += 1

    S = [i for i in range(n) if in_degrees[i] == 0]
    max_size_S = 0

    while S:
        if len(S) > max_size_S:
            max_size_S = len(S)

        alpha = S.pop(0)
        for neighbor in graph[alpha]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                S.append(neighbor)

    return max_size_S

# Read input
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Output
print(topological_sorting(n, m, edges))
```
