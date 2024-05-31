
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def find_parent(root, key):
    if root is None or root.value == key:
        return None
    elif root.left and root.left.value == key or root.right and root.right.value == key:
        return root.value
    elif key < root.value:
        return find_parent(root.left, key)
    else:
        return find_parent(root.right, key)

n = int(input())
numbers = list(map(int, input().split()))

root = Node(numbers[0])
for num in numbers[1:]:
    insert(root, num)

result = []
for i in range(1, n):
    result.append(find_parent(root, numbers[i]))

print(' '.join(map(str, result)))
