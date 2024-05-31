
def can_build_tree(n, nodes):
    total_nodes = sum(nodes)
    if total_nodes != n:
        return "NO"

    for i in range(n):
        if nodes[i] == 1:
            if n - i < 2:
                return "NO"
    
    return "YES"

# Reading input
n = int(input())
nodes = list(map(int, input().split()))

# Check if tree can be built
result = can_build_tree(n, nodes)
print(result)
