
def largest_source_size(n, edges):
    # Initialize a dictionary to store the incoming edges for each node
    in_edges = {i: set() for i in range(n)}
    
    # Count the incoming edges for each node
    for edge in edges:
        in_edges[edge[1]].add(edge[0])
    
    # Find all source nodes (nodes with no incoming edges)
    source_nodes = [node for node in range(n) if len(in_edges[node]) == 0]
    
    # Return the size of the largest set of source nodes
    return max(1, len(source_nodes))

# Read the input parameters
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(largest_source_size(n, edges))
