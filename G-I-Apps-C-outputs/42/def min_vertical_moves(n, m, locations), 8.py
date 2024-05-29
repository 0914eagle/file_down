
def min_vertical_moves(n, m, locations):
    mall_items = [[] for _ in range(m)]
    for x, y, t in locations:
        mall_items[t-1].append((x, y))
    
    min_vertical = float('inf')
    for i in range(m):
        items = mall_items[i]
        dists = []
        for x, y in items:
            if x != 0:
                dists.append(abs(x) - abs(y))
        dists.sort()
        min_vertical = min(min_vertical, sum(dists[:len(dists)//2]))

    return min_vertical

# Example input
n = 3
m = 2
locations = [(1, 1, 2), (1, 2, 1), (-1, 1, 2)]
print(min_vertical_moves(n, m, locations))
```
