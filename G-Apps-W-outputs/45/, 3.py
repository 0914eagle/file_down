
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def find_parent(root, key):
    if root is None or root.key == key:
        return None
    if (root.left and root.left.key == key) or (root.right and root.right.key == key):
        return root.key
    if key < root.key:
        return find_parent(root.left, key)
    return find_parent(root.right, key)

n = int(input())
data = list(map(int, input().split()))

root = Node(data[0])
for i in range(1, n):
    root = insert(root, data[i])

result = []
for i in range(1, n):
    result.append(find_parent(root, data[i]))

print(*result)
