
def distribute_mittens(n, m, colors):
    distinct_pairs = min(colors.count(i) for i in range(1, m+1))
    print(distinct_pairs * 2)
    pairs = [[] for _ in range(distinct_pairs)]
    
    color_indices = {}
    for i in range(n):
        if colors[i] not in color_indices:
            color_indices[colors[i]] = []
        color_indices[colors[i]].append(i+1)
    
    idx = 0
    for color in color_indices:
        for i in range(distinct_pairs):
            pairs[i].append(color)
            pairs[i].append(color_indices[color].pop())
    
    for pair in pairs:
        print(" ".join(map(str, pair)))

# Input parsing
n, m = map(int, input().split())
colors = list(map(int, input().split()))

# Call the function
distribute_mittens(n, m, colors)
```
