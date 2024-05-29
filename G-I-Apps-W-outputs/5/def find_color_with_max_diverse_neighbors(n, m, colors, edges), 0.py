
def find_color_with_max_diverse_neighbors(n, m, colors, edges):
    color_map = {}
    
    for color in colors:
        color_map[color] = set()
    
    for edge in edges:
        a, b = edge
        color_map[colors[a-1]].add(colors[b-1])
        color_map[colors[b-1]].add(colors[a-1])
    
    max_cardinality = 0
    max_color = colors[0]
    
    for color, neighbors in color_map.items():
        cardinality = len(neighbors)
        if cardinality > max_cardinality or (cardinality == max_cardinality and color < max_color):
            max_cardinality = cardinality
            max_color = color
    
    return max_color

# Input parsing
n, m = map(int, input().split())
colors = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

# Calling the function and printing the result
print(find_color_with_max_diverse_neighbors(n, m, colors, edges))
```
