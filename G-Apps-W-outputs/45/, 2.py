
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
            print(root.value, end=' ')
        else:
            insert_node(root.left, value)
    else:
        if root.right is None:
            root.right = Node(value)
            print(root.value, end=' ')
        else:
            insert_node(root.right, value)

def build_binary_search_tree(arr):
    root = Node(arr[0])
    for i in range(1, len(arr)):
        insert_node(root, arr[i])
    print()

n = int(input())
arr = list(map(int, input().split()))

build_binary_search_tree(arr)
