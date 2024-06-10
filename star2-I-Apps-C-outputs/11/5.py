
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return 0
        curr = self.root
        depth = 0
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = Node(val)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(val)
                    break
                curr = curr.right
            depth += 1
        return depth


n = int(input())
bst = BST()
for _ in range(n):
    val = int(input())
    print(bst.insert(val))

