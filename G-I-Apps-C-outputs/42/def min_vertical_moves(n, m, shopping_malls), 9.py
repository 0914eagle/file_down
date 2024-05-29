
def min_vertical_moves(n, m, shopping_malls):
    item_to_mall = {}
    for x, y, t in shopping_malls:
        item_to_mall[t] = (x, y)

    vertical_moves = 0
    for item in range(1, m+1):
        x, y = item_to_mall[item]
        if x < 0 and y > 0:
            x, y = -x, y
        elif x < 0 and y < 0:
            x, y = -x, -y
        elif x > 0 and y < 0:
            x, y = x, -y

        if x > y:
            vertical_moves += 1

    return vertical_moves

# Input parsing
n, m = map(int, input().split())
shopping_malls = [list(map(int, input().split())) for _ in range(n)]

print(min_vertical_moves(n, m, shopping_malls))
```
