
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

def depth(node):
    if node is None:
        return 0
    
    return 1 + max(depth(node.left), depth(node.right))

def solve(arr):
    root = None
    for val in arr:
        root = insert(root, val)
        print(depth(root) - 1)

if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    
    solve(arr)

