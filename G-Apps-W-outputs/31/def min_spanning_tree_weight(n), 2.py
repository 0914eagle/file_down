
def min_spanning_tree_weight(n):
    def get_bitwise_xor(u, v):
        return u ^ v

    # Initialize the weight of the minimum spanning tree to 0
    min_spanning_tree_weight = 0

    # Calculate the weight of the minimum spanning tree
    for u in range(1, n):
        min_spanning_tree_weight += get_bitwise_xor(0, u)

    return min_spanning_tree_weight

# Read input
n = int(input())

# Calculate and print the weight of the minimum spanning tree
print(min_spanning_tree_weight(n))
