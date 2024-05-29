
def distribute_mittens(n, m, colors):
    color_count = {}
    for color in colors:
        color_count[color] = color_count.get(color, 0) + 1

    max_children_with_distinct_mittens = sum(count // 2 for count in color_count.values())
    print(max_children_with_distinct_mittens)

    for color in colors:
        print(color, 1)
        color_count[color] -= 1
        if color_count[color] == 0:
            del color_count[color]
        for other_color, count in color_count.items():
            if count > 0:
                print(other_color, 1)
                color_count[other_color] -= 1
                break

n, m = map(int, input().split())
colors = list(map(int, input().split()))
distribute_mittens(n, m, colors)
```
