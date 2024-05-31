
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

def find_parent(root, key, parent=None):
    if root is None:
        return None
    if root.key == key:
        return parent
    if key < root.key:
        return find_parent(root.left, key, root.key)
    return find_parent(root.right, key, root.key)

def solve(n, nums):
    root = Node(nums[0])
    parent_list = []
    for num in nums[1:]:
        root = insert(root, num)
        parent = find_parent(root, num)
        parent_list.append(parent)
    return parent_list

# Input processing
n = int(input())
nums = list(map(int, input().split()))

# Solve the problem
result = solve(n, nums)

# Output the result
for parent in result:
    print(parent, end=' ')

