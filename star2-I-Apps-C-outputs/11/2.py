
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(node, val):
    if node is None:
        return Node(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

def dfs(node, depth):
    if node is None:
        return 0
    return dfs(node.left, depth+1) + dfs(node.right, depth+1) + depth

n = int(input())
root = None
for _ in range(n):
    val = int(input())
    root = insert(root, val)
print(dfs(root, 0))

