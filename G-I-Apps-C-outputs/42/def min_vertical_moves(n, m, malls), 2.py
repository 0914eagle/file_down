
def min_vertical_moves(n, m, malls):
    item_to_mall = {mall[2]: (mall[0], mall[1]) for mall in malls}
    vertical_moves = 0
    for item in range(1, m + 1):
        x, y = item_to_mall[item]
        if (x > 0 and y > 0) or (x < 0 and y < 0):
            vertical_moves += 1
    return vertical_moves

# Input parsing and function call
n, m = map(int, input().split())
malls = [list(map(int, input().split())) for _ in range(n)]
print(min_vertical_moves(n, m, malls))
```
