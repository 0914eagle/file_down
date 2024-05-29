
def solve_maximum_degree_spanning_tree(n, m, edges):
    adj_list = [[] for _ in range(n)]
    degrees = [0] * n
    
    for edge in edges:
        u, v = edge
        adj_list[u - 1].append(v)
        adj_list[v - 1].append(u)
        degrees[u - 1] += 1
        degrees[v - 1] += 1
    
    max_deg_vertex = degrees.index(max(degrees))
    tree_edges = []
    visited = [False] * n
    visited[max_deg_vertex] = True
    
    queue = [max_deg_vertex]
    while queue:
        cur_vertex = queue.pop(0)
        for neighbor in adj_list[cur_vertex]:
            if not visited[neighbor - 1]:
                visited[neighbor - 1] = True
                tree_edges.append((cur_vertex + 1, neighbor))
                queue.append(neighbor)
    
    return tree_edges

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
result = solve_maximum_degree_spanning_tree(n, m, edges)
for edge in result:
    print(edge[0], edge[1])
```
