
def can_build_tree(n, nodes):
    total_nodes = sum(nodes)
    max_internal_nodes = total_nodes - n
    if max(nodes) > max_internal_nodes:
        return "NO"
    return "YES"

# Input
n = int(input())
nodes = list(map(int, input().split()))

# Output
print(can_build_tree(n, nodes))
