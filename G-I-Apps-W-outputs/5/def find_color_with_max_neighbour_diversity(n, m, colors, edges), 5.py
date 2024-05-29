
def find_color_with_max_neighbour_diversity(n, m, colors, edges):
    color_neighbors = {}  # dictionary to store the count of different colors neighboring each color
    max_diversity = 0
    result_color = None

    for color in set(colors):
        color_neighbors[color] = set()

    for edge in edges:
        v1, v2 = edge
        if colors[v1-1] != colors[v2-1]:
            color_neighbors[colors[v1-1]].add(colors[v2-1])
            color_neighbors[colors[v2-1]].add(colors[v1-1])

    for color, neighbors in color_neighbors.items():
        if len(neighbors) > max_diversity:
            max_diversity = len(neighbors)
            result_color = color

    return result_color

# Input parsing
n, m = map(int, input().split())
colors = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

# Call the function with input values
result = find_color_with_max_neighbour_diversity(n, m, colors, edges)
print(result)
```
