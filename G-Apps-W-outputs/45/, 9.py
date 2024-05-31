
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_parent(root, key):
    if root.key == key:
        return None
    elif (root.left and root.left.key == key) or (root.right and root.right.key == key):
        return root.key
    elif key < root.key:
        return find_parent(root.left, key)
    else:
        return find_parent(root.right, key)

def find_parents(arr):
    n = len(arr)
    if n < 2:
        return []

    root = Node(arr[0])
    result = []
    for i in range(1, n):
        root = insert(root, arr[i])
        parent = find_parent(root, arr[i])
        result.append(parent)
    return result

n = int(input())
numbers = list(map(int, input().split()))
parents = find_parents(numbers)
print(" ".join(map(str, parents)))
