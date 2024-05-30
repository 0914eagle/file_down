
from collections import defaultdict

def solve_tree_queries(n, m, edges, queries):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    parent = {1: -1}
    stack = [1]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor != parent[node]:
                parent[neighbor] = node
                stack.append(neighbor)

    def is_valid_path(u, query):
        for v in query:
            if v == u or v == 1:
                continue
            if parent[v] != u and parent[u] != v:
                return False
        return True

    for query in queries:
        k = query[0]
        vertices = query[1:]
        found = False
        for u in vertices:
            if is_valid_path(u, vertices):
                found = True
                break
        if found:
            print("YES")
        else:
            print("NO")

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
queries = [list(map(int, input().split()))[1:] for _ in range(m)]

# Calling the function with input values
solve_tree_queries(n, m, edges, queries)
```
