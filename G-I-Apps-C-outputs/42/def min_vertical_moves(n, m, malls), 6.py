
def min_vertical_moves(n, m, malls):
    items_to_malls = {i+1: [] for i in range(m)}
    for mall in malls:
        items_to_malls[mall[2]].append((mall[0], mall[1]))

    vertical_moves = 0
    for item, mall_positions in items_to_malls.items():
        minX = min(mall_positions, key=lambda p: p[0])[0]
        minY = min(mall_positions, key=lambda p: p[1])[1]
        maxX = max(mall_positions, key=lambda p: p[0])[0]
        maxY = max(mall_positions, key=lambda p: p[1])[1]

        if abs(maxX - minX) < abs(maxY - minY):
            vertical_moves += 1

    return vertical_moves

# Read input
n, m = map(int, input().split())
malls = [list(map(int, input().split())) for _ in range(n)]

# Get minimum number of vertical moves
result = min_vertical_moves(n, m, malls)
print(result)
```
