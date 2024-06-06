
from collections import deque
n = int(input())
my_list = []
for i in range(n):
    my_list.append(list(map(int, input().split())))

root_set = set()
root_set.add(0)

class Node:
    def __init__(self, name):
        self.name = name
        self.child = []
        self.parent = []

class Tree:
    def __init__(self):
        self.nodes = []
        for i in range(n):
            self.nodes.append(Node(i))

    def add_node(self, parent, child):
        self.nodes[parent].child.append(child)
        self.nodes[child].parent.append(parent)

tree = Tree()

for i in range(n):
    for j in range(1, my_list[i][0] + 1):
        for k in range(n):
            if my_list[i][j] in my_list[k]:
                tree.add_node(i, k)

q = deque()
q.append(0)
visited = set()
visited.add(0)

while q:
    cur = q.popleft()
    if cur not in root_set:
        print("impossible")
        exit(0)
    for child in tree.nodes[cur].child:
        if child not in visited:
            visited.add(child)
            q.append(child)

for i in range(n):
    for child in tree.nodes[i].child:
        print(i + 1, child + 1, my_list[child][1])

