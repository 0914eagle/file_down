
def find_max_degree_spanning_tree(n, m, edges):
    adj_list = {}
    degrees = [0] * n

    for i in range(n):
        adj_list[i+1] = []

    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
        degrees[u-1] += 1
        degrees[v-1] += 1

    max_degree = max(degrees)
    max_vertex = degrees.index(max_degree) + 1

    tree_edges = []
    visited = [False] * n
    visited[max_vertex-1] = True

    stack = [max_vertex]
    while stack:
        curr_vertex = stack.pop()
        for neighbor in adj_list[curr_vertex]:
            if not visited[neighbor-1]:
                tree_edges.append((curr_vertex, neighbor))
                visited[neighbor-1] = True
                stack.append(neighbor)

    return tree_edges

# Input example
n, m = 5, 5
edges = [(1, 2), (2, 3), (3, 5), (4, 3), (1, 5)]
result = find_max_degree_spanning_tree(n, m, edges)

for edge in result:
    print(*edge)
```
