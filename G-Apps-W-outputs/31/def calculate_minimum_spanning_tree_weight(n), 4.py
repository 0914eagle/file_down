
def calculate_minimum_spanning_tree_weight(n):
    def xor_weight(u, v):
        return u ^ v
    
    total_weight = 0
    for i in range(1, n):
        total_weight += xor_weight(0, i)
    
    return total_weight

# Read input
n = int(input())

# Calculate and print the weight of the minimum spanning tree
print(calculate_minimum_spanning_tree_weight(n))
