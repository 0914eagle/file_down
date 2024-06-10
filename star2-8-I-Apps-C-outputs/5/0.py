
class Node:
  def __init__(self):
    self.children = []
    self.marked = False
    
class Tree:
  def __init__(self):
    self.root = Node()
  def mark(self, D):
    queue = [self.root]
    while queue:
      curr = queue.pop(0)
      curr.marked = True
      for child in curr.children:
        queue.append(child)
        for i in range(D-1):
          if queue:
            queue.pop(0).marked = True
  def count_marked(self):
    queue = [self.root]
    count = 0
    while queue:
      curr = queue.pop(0)
      if curr.marked:
        count += 1
      for child in curr.children:
        queue.append(child)
    return count
    
N, D = map(int, input().split())
tree = Tree()
for i in range(N-1):
  x = int(input())
  tree.root.children.append(Node())
  tree.root.children[-1].children.append(tree.root)
tree.mark(D)
print(tree.count_marked())

