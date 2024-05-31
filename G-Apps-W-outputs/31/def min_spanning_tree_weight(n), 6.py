
def min_spanning_tree_weight(n):
    # Function to calculate the xor value between two numbers
    def xor(u, v):
        return u ^ v
    
    # Initialize the weight of the minimum spanning tree
    total_weight = 0
    
    for i in range(1, n):
        # Calculate the weight of the edge between vertices 0 and i
        weight = xor(0, i)
        total_weight += weight
    
    return total_weight

# Read input
n = int(input())

# Calculate and output the weight of the minimum spanning tree
print(min_spanning_tree_weight(n))
