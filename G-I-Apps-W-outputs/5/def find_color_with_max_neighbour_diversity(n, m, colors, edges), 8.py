
def find_color_with_max_neighbour_diversity(n, m, colors, edges):
    neighbors = {}
    max_diversity = -1
    max_color = max(colors)
    
    for i in range(1, n+1):
        neighbors[i] = set()
    
    for edge in edges:
        a, b = edge
        if colors[a-1] != colors[b-1]:
            neighbors[a].add(colors[b-1])
            neighbors[b].add(colors[a-1])
    
    for i in range(1, n+1):
        diversity = len(neighbors[i])
        if diversity > max_diversity or (diversity == max_diversity and colors[i-1] < max_color):
            max_diversity = diversity
            max_color = colors[i-1]
    
    return max_color

# Reading input
n, m = map(int, input().split())
colors = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Calling the function and printing the output
print(find_color_with_max_neighbour_diversity(n, m, colors, edges))
```
