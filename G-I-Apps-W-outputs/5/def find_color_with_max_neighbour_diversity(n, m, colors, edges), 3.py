
def find_color_with_max_neighbour_diversity(n, m, colors, edges):
    neighbor_diversity = {}
    
    for color in set(colors):
        neighbor_colors = set()
        for edge in edges:
            if colors[edge[0]-1] == color:
                neighbor_colors.add(colors[edge[1]-1])
            elif colors[edge[1]-1] == color:
                neighbor_colors.add(colors[edge[0]-1])
        neighbor_diversity[color] = len(neighbor_colors)
    
    max_diversity = max(neighbor_diversity.values())
    max_diversity_colors = [color for color, div in neighbor_diversity.items() if div == max_diversity]
    
    return min(max_diversity_colors)

# Input reading
n, m = map(int, input().split())
colors = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(find_color_with_max_neighbour_diversity(n, m, colors, edges))
```
