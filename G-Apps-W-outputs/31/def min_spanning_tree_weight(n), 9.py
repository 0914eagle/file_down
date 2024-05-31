
def min_spanning_tree_weight(n):
    # Bitwise XOR of two consecutive numbers always gives 1
    # Therefore, the weight of the edge between vertices u and v is always 1 for u < v
    # The minimum spanning tree will have n-1 edges, each with weight 1
    return n - 1

# Read input
n = int(input().strip())

# Calculate and output the weight of the minimum spanning tree
print(min_spanning_tree_weight(n))
