
def find_color_with_max_diverset(neighbors, colors):
    max_diversity = 0
    max_color = float("inf")
    
    for color in colors:
        color_neighbors = set()
        for neighbor in neighbors:
            if colors[neighbor] != color:
                color_neighbors.add(colors[neighbor])
        
        diversity = len(color_neighbors)
        if diversity > max_diversity or (diversity == max_diversity and color < max_color):
            max_diversity = diversity
            max_color = color
    
    return max_color

# Read input
n, m = map(int, input().split())
colors = list(map(int, input().split()))

neighbors = []
for _ in range(m):
    a, b = map(int, input().split())
    neighbors.append(a-1)
    neighbors.append(b-1)

# Find color with maximum diverse neighbors
result = find_color_with_max_diverset(neighbors, colors)
print(result)
```
