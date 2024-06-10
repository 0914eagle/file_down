
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


def depth(node, val, d):
    if node is None:
        return 0
    if node.val == val:
        return d
    if val < node.val:
        return depth(node.left, val, d + 1)
    return depth(node.right, val, d + 1)


def solve(seq):
    root = None
    for val in seq:
        root = insert(root, val)
        print(depth(root, val, 0))


if __name__ == "__main__":
    n = int(input())
    seq = [int(input()) for _ in range(n)]
    solve(seq)

