
def solve_party_mittens(n, m, mittens):
    colors_count = [0] * m
    for color in mittens:
        colors_count[color - 1] += 1

    max_children_pairs = min(colors_count)

    print(max_children_pairs)

    for color_idx in range(m):
        for i in range(max_children_pairs):
            print(color_idx + 1, (color_idx + 1) % m + 1)

n, m = map(int, input().split())
mittens = list(map(int, input().split()))

solve_party_mittens(n, m, mittens)
```
