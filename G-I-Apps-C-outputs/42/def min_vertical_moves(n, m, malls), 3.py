
def min_vertical_moves(n, m, malls):
    items_to_mall = {}
    for mall in malls:
        x, y, item = mall
        if item not in items_to_mall:
            items_to_mall[item] = []
        items_to_mall[item].append((x, y))

    min_vertical_moves = 0
    for item, locations in items_to_mall.items():
        if len(locations) == 1:
            continue

        sorted_by_x = sorted(locations, key=lambda x: x[0])
        mid_x = sorted_by_x[len(sorted_by_x) // 2][0]

        vertical_moves = sum(1 for x, _ in locations if x < mid_x) if len(locations) % 2 == 0 else 0
        min_vertical_moves += vertical_moves

    return min_vertical_moves

# Input parsing
n, m = map(int, input().split())
malls = []
for _ in range(n):
    x, y, t = map(int, input().split())
    malls.append((x, y, t))

# Call the function
result = min_vertical_moves(n, m, malls)
print(result)
```
