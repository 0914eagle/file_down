
def distribute_mittens(n, m, colors):
    unique_colors = set(colors)
    max_children = min(len(unique_colors), n)
    
    color_pairs = []
    for i in range(n):
        color_pairs.append((colors[i], list(unique_colors - {colors[i]})[0]))
    
    print(max_children)
    for pair in color_pairs:
        print(pair[0], pair[1])

# Sample Input
n, m = 4, 2
colors = [1, 2, 1, 1]
distribute_mittens(n, m, colors)
```
