
from collections import defaultdict

def count_odd_colors(colors):
    color_count = defaultdict(int)
    odd_count = 0
    for color in colors:
        color_count[color] += 1
    for count in color_count.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count

def count_magical_colors(colors, tree, node):
    subtree_colors = []
    subtree_nodes = [node]
    while subtree_nodes:
        current_node = subtree_nodes.pop()
        subtree_colors.append(colors[current_node - 1])
        subtree_nodes.extend(tree[current_node])
    return count_odd_colors(subtree_colors)

N, Q = map(int, input().split())
colors = list(map(int, input().split()))
tree = defaultdict(list)
for _ in range(N-1):
    parent, child = map(int, input().split())
    tree[parent].append(child)

for _ in range(Q):
    K, X = map(int, input().split())
    if K == 0:
        print(count_magical_colors(colors, tree, X))
    else:
        colors[X - 1] = K
```
