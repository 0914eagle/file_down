
def find_color_with_max_neighbour_diversity(n, m, colors, edges):
    color_counts = {}
    max_diversity_color = None
    max_diversity = 0

    for c in colors:
        color_counts[c] = 0

    for a, b in edges:
        if colors[a - 1] != colors[b - 1]:
            color_counts[colors[a - 1]] += 1
            color_counts[colors[b - 1]] += 1

    for c, count in color_counts.items():
        if count > max_diversity or (count == max_diversity and c < max_diversity_color):
            max_diversity = count
            max_diversity_color = c

    return max_diversity_color

# Input parsing
n, m = map(int, input().split())
colors = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

print(find_color_with_max_neighbour_diversity(n, m, colors, edges))
```
