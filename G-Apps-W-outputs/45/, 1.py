
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_node(root, val):
    if val < root.val:
        if root.left is None:
            root.left = TreeNode(val)
            return root.val
        else:
            return insert_node(root.left, val)
    else:
        if root.right is None:
            root.right = TreeNode(val)
            return root.val
        else:
            return insert_node(root.right, val)

def find_parent(root, val):
    if val < root.val:
        if root.left is not None and root.left.val == val:
            return root.val
        else:
            return find_parent(root.left, val)
    else:
        if root.right is not None and root.right.val == val:
            return root.val
        else:
            return find_parent(root.right, val)

def find_parents(arr):
    if not arr:
        return []

    root = TreeNode(arr[0])
    parents = [None] * len(arr)
    parents[0] = None

    for i in range(1, len(arr)):
        parents[i] = insert_node(root, arr[i])

    return parents[1:]

n = int(input())
numbers = list(map(int, input().split()))

parents = find_parents(numbers)
print(' '.join(map(str, parents)))
