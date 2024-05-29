
def is_k_multihedgehog(n, k, edges):
    degrees = [0] * (n + 1)
    neighbors = [set() for _ in range(n + 1)]

    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
        neighbors[u].add(v)
        neighbors[v].add(u)

    leaf_nodes = [node for node in range(1, n+1) if degrees[node] == 1]
    center_node = [node for node in range(1, n+1) if degrees[node] >= 3]

    if len(center_node) != 1:
        return "No"

    center = center_node[0]
    for _ in range(k):
        new_leaf_nodes = []
        for leaf in leaf_nodes:
            if degrees[leaf] == 1:
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                degrees[leaf] -= 1
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    new_leaf_nodes.append(neighbor)
        leaf_nodes = new_leaf_nodes

    return "Yes" if len(leaf_nodes) == 0 else "No"


# Input
n, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n - 1)]

# Output
print(is_k_multihedgehog(n, k, edges))
