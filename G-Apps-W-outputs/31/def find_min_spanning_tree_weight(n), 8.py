
def find_min_spanning_tree_weight(n):
    def find_xor_sum(x):
        if x % 4 == 0:
            return x
        if x % 4 == 1:
            return 1
        if x % 4 == 2:
            return x + 1
        return 0
    
    xor_sum = find_xor_sum(n)  # Calculate the xor sum of the complete graph
    return xor_sum

# Read input
n = int(input().strip())

# Find and output the weight of the minimum spanning tree
print(find_min_spanning_tree_weight(n))
