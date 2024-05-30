
class Node:
    def __init__(self, color):
        self.color = color
        self.children = []
        self.magical_colors = [0] * 101

def update_magical_colors(node):
    node.magical_colors[node.color] = 1
    for child in node.children:
        update_magical_colors(child)
        for i in range(1, 101):
            node.magical_colors[i] += child.magical_colors[i]

def change_color(node, new_color):
    node.magical_colors[node.color] -= 1
    node.color = new_color
    node.magical_colors[node.color] += 1

def query_magical_colors(node):
    return sum(1 for x in node.magical_colors if x % 2 == 1)

# Read input
N, Q = map(int, input().split())
colors = list(map(int, input().split()))
parents = list(map(int, input().split()))

nodes = [Node(color) for color in colors]

for i in range(1, N):
    parent = parents[i-1]
    nodes[parent-1].children.append(nodes[i])

update_magical_colors(nodes[0])

for _ in range(Q):
    K, X = map(int, input().split())
    if K == 0:
        print(query_magical_colors(nodes[X-1]))
    else:
        change_color(nodes[X-1], K)
        update_magical_colors(nodes[0])
```
