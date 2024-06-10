
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

def depth(node, val):
    if node is None:
        return 0
    if val < node.val:
        return depth(node.left, val) + 1
    else:
        return depth(node.right, val) + 1

def solve(seq):
    root = None
    counter = 0
    for val in seq:
        root = insert(root, val)
        counter += depth(root, val)
        print(counter)

n = int(input())
seq = [int(input()) for _ in range(n)]
solve(seq)

