
# Using a simple approach to construct a spanning tree with maximum possible degree

from collections import defaultdict

def construct_spanning_tree(n, edges):
    adj_list = defaultdict(list)
    degree = [0] * (n+1)

    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
        degree[u] += 1
        degree[v] += 1

    max_degree_vertex = max(range(1, n+1), key=lambda x: degree[x])

    visited = [False] * (n+1)
    visited[max_degree_vertex] = True

    tree_edges = []
    for neighbor in adj_list[max_degree_vertex]:
        tree_edges.append((max_degree_vertex, neighbor))
        visited[neighbor] = True

    for edge in edges:
        u, v = edge
        if u != max_degree_vertex and v != max_degree_vertex and not visited[u] and not visited[v]:
            tree_edges.append((u, v))
            visited[u] = True
            visited[v] = True

    return tree_edges


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = construct_spanning_tree(n, edges)
for edge in result:
    print(edge[0], edge[1])
```
