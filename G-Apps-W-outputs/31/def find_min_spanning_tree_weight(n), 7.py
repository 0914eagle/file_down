
def find_min_spanning_tree_weight(n):
    x = 0
    i = 1
    while i * 2 <= n:
        x += i
        i *= 2
    if i != n:
        x += n - i
    return x

# Read input
n = int(input().strip())

# Find and output the weight of the minimum spanning tree
print(find_min_spanning_tree_weight(n))
