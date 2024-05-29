
def find_max_diverse_color(n, m, colors, edges):
    neighbor_colors = {}
    
    for color in set(colors):
        neighbor_colors[color] = set()
    
    for edge in edges:
        a, b = edge
        if colors[a-1] != colors[b-1]:
            neighbor_colors[colors[a-1]].add(colors[b-1])
            neighbor_colors[colors[b-1]].add(colors[a-1])
    
    max_diversity = -1
    max_color = float('inf')
    
    for color, neighbors in neighbor_colors.items():
        diversity = len(neighbors)
        if diversity > max_diversity or (diversity == max_diversity and color < max_color):
            max_diversity = diversity
            max_color = color
            
    return max_color

# Input processing
n, m = map(int, input().split())
colors = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

print(find_max_diverse_color(n, m, colors, edges))
```
