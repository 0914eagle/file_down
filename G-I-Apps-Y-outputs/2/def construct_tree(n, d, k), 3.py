
from collections import deque

def construct_tree(n, d, k):
    if d >= n:
        return "NO"
    
    if d == 1 and n > 2:
        return "NO"
    
    if k < 2:
        return "NO"
    
    if k == 2 and n > 2:
        return "NO"
    
    if k == 1 and n > 2:
        return "NO"
    
    tree = []
    curr_node = 2
    depth = 1
    
    for i in range(n - 1):
        tree.append((curr_node, curr_node - 1))
        if depth < d:
            curr_node += 1
            depth += 1
        elif depth == d:
            curr_node = 2
            depth = 1
    
    return "YES\n" + "\n".join(["{} {}".format(u, v) for u, v in tree])

# Input
n, d, k = map(int, input().split())

# Output
print(construct_tree(n, d, k))
