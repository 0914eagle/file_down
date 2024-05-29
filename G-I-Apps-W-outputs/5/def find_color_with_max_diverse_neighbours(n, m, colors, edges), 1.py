
def find_color_with_max_diverse_neighbours(n, m, colors, edges):
    color_counts = {}
    neighbor_colors = {}

    for i in range(1, n+1):
        color_counts[i] = 0

    for edge in edges:
        a, b = edge
        if colors[a-1] != colors[b-1]:
            color_counts[colors[a-1]] += 1
            color_counts[colors[b-1]] += 1
            if colors[b-1] not in neighbor_colors:
                neighbor_colors[colors[b-1]] = set()
            neighbor_colors[colors[b-1]].add(colors[a-1])
            if colors[a-1] not in neighbor_colors:
                neighbor_colors[colors[a-1]] = set()
            neighbor_colors[colors[a-1]].add(colors[b-1])

    max_diverse_neighbors = 0
    color_with_max_diverse_neighbors = float('inf')

    for color in range(1, n+1):
        if color_counts[color] > max_diverse_neighbors:
            max_diverse_neighbors = color_counts[color]
            color_with_max_diverse_neighbors = color
        elif color_counts[color] == max_diverse_neighbors:
            if color < color_with_max_diverse_neighbors:
                color_with_max_diverse_neighbors = color

    return color_with_max_diverse_neighbors

# Example Input
n, m = 6, 6
colors = [1, 1, 2, 3, 5, 8]
edges = [(1, 2), (3, 2), (1, 4), (4, 3), (4, 5), (4, 6)]

print(find_color_with_max_diverse_neighbours(n, m, colors, edges))

n, m = 5, 6
colors = [4, 2, 5, 2, 4]
edges = [(1, 2), (2, 3), (3, 1), (5, 3), (5, 4), (3, 4)]

print(find_color_with_max_diverse_neighbours(n, m, colors, edges))
```
