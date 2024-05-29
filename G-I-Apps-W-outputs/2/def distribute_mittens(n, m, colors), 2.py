
def distribute_mittens(n, m, colors):
    color_counts = {}
    for color in colors:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    max_children = min(color_counts.values())

    print(max_children)
    for color in range(1, m+1):
        for _ in range(max_children):
            print(f"{color} {next((c for c in range(1, m+1) if c != color and color_counts[c] > 0), color)}")
            color_counts[color] -= 1

# Input parsing
n, m = map(int, input().split())
colors = list(map(int, input().split()))

distribute_mittens(n, m, colors)
```
