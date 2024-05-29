
def solve_mitten_exchange(n, m, mittens_colors):
    colors_count = {}
    for color in mittens_colors:
        if color in colors_count:
            colors_count[color] += 1
        else:
            colors_count[color] = 1
    
    max_children_with_distinct_mittens = min(len(colors_count), n)
    
    print(max_children_with_distinct_mittens)
    
    for i in range(n):
        print(f"{mittens_colors[i]} {list(set(colors_count.keys()) - set([mittens_colors[i]]))[0]}")

# Input
n, m = map(int, input().split())
mittens_colors = list(map(int, input().split()))

# Solve and output result
solve_mitten_exchange(n, m, mittens_colors)
```
