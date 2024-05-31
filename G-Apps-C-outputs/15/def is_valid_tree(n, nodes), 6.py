
def is_valid_tree(n, nodes):
    total = sum(nodes)
    if total != n:
        return "NO"
    
    for node in nodes:
        if node == 1 or node > n:
            return "NO"
    
    return "YES"

# Reading input
n = int(input())
nodes = list(map(int, input().split()))

# Calling the function and printing the result
print(is_valid_tree(n, nodes))
