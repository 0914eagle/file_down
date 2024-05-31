
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_parent(root, key):
    while root is not None:
        if root.val < key:
            if root.right is not None and root.right.val == key:
                return root.val
            root = root.right
        else:
            if root.left is not None and root.left.val == key:
                return root.val
            root = root.left

n = int(input())
numbers = list(map(int, input().split()))

root = Node(numbers[0])

for i in range(1, n):
    root = insert(root, numbers[i])

result = []
for i in range(1, n):
    result.append(find_parent(root, numbers[i]))

print(' '.join(map(str, result)))
