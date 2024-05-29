
def min_vertical_moves(n, m, malls):
    item_positions = {}  # Dictionary to store item positions
    for x, y, t in malls:
        item_positions[t] = (x, y)

    vertical_moves = 0
    for i in range(1, m + 1):
        x, y = item_positions[i]
        if abs(x) < abs(y):
            vertical_moves += 1

    return vertical_moves

# Reading input
n, m = map(int, input().split())
malls = []
for _ in range(n):
    x, y, t = map(int, input().split())
    malls.append((x, y, t))

# Calling the function and printing the output
print(min_vertical_moves(n, m, malls))
```
