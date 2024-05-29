
def find_color_with_max_neighbour_diversity(n, m, colors, edges):
    color_neighbors = {}
    for color in set(colors):
        color_neighbors[color] = set()
    
    for edge in edges:
        a, b = edge
        if colors[a-1] != colors[b-1]:
            color_neighbors[colors[a-1]].add(colors[b-1])
            color_neighbors[colors[b-1]].add(colors[a-1])

    max_diversity = 0
    max_color = float('inf')
    for color, neighbors in color_neighbors.items():
        diversity = len(neighbors)
        if diversity > max_diversity or (diversity == max_diversity and color < max_color):
            max_diversity = diversity
            max_color = color

    return max_color

# Input parsing
n, m = map(int, input().split())
colors = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function with the input
result = find_color_with_max_neighbour_diversity(n, m, colors, edges)
print(result)
```
