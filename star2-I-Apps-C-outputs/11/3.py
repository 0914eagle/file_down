
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(node, val):
    if val < node.val:
        if node.left is None:
            node.left = Node(val)
            return 1
        else:
            return 1 + insert(node.left, val)
    else:
        if node.right is None:
            node.right = Node(val)
            return 1
        else:
            return 1 + insert(node.right, val)

def solve(arr):
    root = Node(arr[0])
    counter = 0
    for val in arr[1:]:
        counter += insert(root, val)
        print(counter)

if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    solve(arr)

