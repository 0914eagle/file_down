
from collections import defaultdict

def find_max_degree_spanning_tree(n, m, edges):
    adj_list = defaultdict(list)
    degrees = defaultdict(int)
    tree_edges = []

    for v, u in edges:
        adj_list[v].append(u)
        adj_list[u].append(v)
        degrees[v] += 1
        degrees[u] += 1

    max_degree_vertex = max(degrees, key=degrees.get)

    visited = set()
    stack = [max_degree_vertex]
    visited.add(max_degree_vertex)

    while stack:
        current_vertex = stack.pop()
        for neighbor in adj_list[current_vertex]:
            if neighbor not in visited:
                tree_edges.append((current_vertex, neighbor))
                visited.add(neighbor)
                stack.append(neighbor)

    return tree_edges

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = find_max_degree_spanning_tree(n, m, edges)

for edge in result:
    print(edge[0], edge[1])
```
