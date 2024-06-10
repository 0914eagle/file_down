
class Node:
  def __init__(self):
    self.children = []
    self.depth = 0
def dfs(node):
  if len(node.children) == 0:
    return
  for child in node.children:
    child.depth = node.depth + 1
    dfs(child)
def bfs(start_node, max_depth):
  queue = [start_node]
  marked = 1
  while len(queue) > 0:
    node = queue.pop(0)
    for child in node.children:
      if child.depth > max_depth:
        marked += 1
        queue.append(child)
  return marked
def solve():
  n, d = map(int, input().split())
  nodes = [Node() for _ in range(n)]
  for i in range(1, n):
    nodes[i].children.append(nodes[int(input())])
  dfs(nodes[0])
  return bfs(nodes[0], d)
print(solve())

