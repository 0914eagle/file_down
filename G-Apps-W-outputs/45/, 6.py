
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def find_parent(root, key, parent=None):
    if root is None:
        return None
    if root.data == key:
        return parent
    if key < root.data:
        return find_parent(root.left, key, root.data)
    return find_parent(root.right, key, root.data)

def create_tree(arr):
    if not arr:
        return None
    root = Node(arr[0])
    for i in range(1, len(arr)):
        insert(root, arr[i])
    return root

def find_parents_in_tree(arr):
    root = create_tree(arr)
    result = []
    for i in range(1, len(arr)):
        parent = find_parent(root, arr[i])
        result.append(parent)
    return result

n = int(input())
numbers = list(map(int, input().split()))
parents = find_parents_in_tree(numbers)
print(" ".join(map(str, parents)))
