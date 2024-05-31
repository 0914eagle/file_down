
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
            return root.value
        else:
            return insert(root.left, value)
    else:
        if root.right is None:
            root.right = Node(value)
            return root.value
        else:
            return insert(root.right, value)

def find_parent(root, value):
    if value < root.value:
        if root.left.value == value:
            return root.value
        else:
            return find_parent(root.left, value)
    else:
        if root.right.value == value:
            return root.value
        else:
            return find_parent(root.right, value)

n = int(input())
numbers = list(map(int, input().split()))

root = Node(numbers[0])
parents = []

for num in numbers[1:]:
    parent = insert(root, num)
    parents.append(parent)

print(' '.join(map(str, parents)))
