
def construct_tree(n, d, k):
    if d >= n:
        return "NO"
    if k == 1:
        if n == 1:
            return "YES"
        else:
            return "NO"
    if d == 1:
        if n > 2:
            return "NO"
        else:
            return "YES\n1 2"

    edges = []
    for i in range(2, d + 2):
        edges.append((1, i))

    curr_node = 2
    remaining_vertices = n - (d + 1)

    while remaining_vertices > 0:
        for i in range(2, min(k + 1, remaining_vertices) + 1):
            edges.append((curr_node, curr_node + i - 1))
            remaining_vertices -= 1

        curr_node += 1

    if remaining_vertices == 0:
        return "YES\n" + "\n".join([f"{edge[0]} {edge[1]}" for edge in edges])
    else:
        return "NO"


# Read input
n, d, k = map(int, input().split())

# Output result
print(construct_tree(n, d, k))
```
