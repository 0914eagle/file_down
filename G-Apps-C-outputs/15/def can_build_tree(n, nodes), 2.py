
def can_build_tree(n, nodes):
    total_nodes = sum(nodes)
    if total_nodes != n:
        return "NO"
    for node in nodes:
        if node == 1 or node > n:
            return "NO"
    return "YES"

# Input
n = 4
nodes = [1, 1, 1, 4]

# Output
print(can_build_tree(n, nodes))

n = 5
nodes = [1, 1, 5, 2, 1]
print(can_build_tree(n, nodes))
