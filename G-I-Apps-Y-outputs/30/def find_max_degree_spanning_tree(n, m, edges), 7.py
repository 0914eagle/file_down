
def find_max_degree_spanning_tree(n, m, edges):
    # Initialize an empty dictionary to store the degree of each vertex
    degrees = {i: 0 for i in range(1, n + 1)}
    
    # Initialize an empty list to store the selected edges of the spanning tree
    tree_edges = []
    
    # Sort the edges by decreasing order of the sum of degrees of their vertices
    edges.sort(key=lambda x: degrees[x[0]] + degrees[x[1]], reverse=True)
    
    # Loop through the edges and add them to the spanning tree if they increase the maximum degree
    for edge in edges:
        v, u = edge
        if degrees[v] < 2 and degrees[u] < 2:
            tree_edges.append((v, u))
            degrees[v] += 1
            degrees[u] += 1
    
    return tree_edges

# Input processing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
spanning_tree = find_max_degree_spanning_tree(n, m, edges)
for edge in spanning_tree:
    print(edge[0], edge[1])
```
